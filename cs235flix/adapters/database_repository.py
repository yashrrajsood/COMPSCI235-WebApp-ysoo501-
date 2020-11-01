import csv
import os

from datetime import date
from typing import List

from sqlalchemy import desc, asc
from sqlalchemy.engine import Engine
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from werkzeug.security import generate_password_hash

from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack

from cs235flix.domain.model import User, Movie, Review, Genre, Actor, Director, WatchList
from cs235flix.adapters.repository import AbstractRepository


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

    def get_user(self, username) -> User:
        user = None
        try:
            user = self._session_cm.session.query(User).filter_by(_username=username).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return user

    def add_movie(self, movie: Movie):
        with self._session_cm as scm:
            scm.session.add(movie)
            scm.commit()

    def get_movie(self, id: int) -> Movie:
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter(Movie._rank == id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return movie

    def get_all_movies(self):
        movies = None
        try:
            movies = self._session_cm.session.query(Movie).all()
        except NoResultFound:
            pass
        return movies

    def add_genre(self, genre: Genre):
        with self._session_cm as scm:
            scm.session.add(genre)
            scm.commit()

    def get_genres(self):
        genres = None
        try:
            genres = self._session_cm.session.query(Genre).all()
        except NoResultFound:
            pass
        return genres

    def get_directors(self):
        pass

    def add_director(self, director: Director):
        pass

    def add_actor(self, actor: Actor):
        with self._session_cm as scm:
            scm.session.add(actor)
            scm.commit()

    def get_actors(self):
        actors = None
        try:
            actors = self._session_cm.session.query(Actor).all()
        except NoResultFound:
            pass
        return actors

    def get_all_movies_by_rank(self):
        movies = None
        try:
            movies = self._session_cm.session.query(Movie).all()
        except NoResultFound:
            pass
        temp = sorted(movies, key=lambda x: x.rank)
        return movies

    def get_movie_by_name(self, id):
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter(Movie._rank == id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return movie

    def get_genre_by_name(self, name):
        genre = None
        try:
            genre = self._session_cm.session.query(Genre).filter(Genre.genre_name == name).one()
        except NoResultFound:
            pass
        return genre

    def get_movies_by_genre(self, genre_name):
        pass

    def get_movies_by_actor(self, name):
        pass

    def get_movies_by_director(self, name):
        pass

    def get_user_watchlist(self, user):
        watchlist = None
        try:
            watchlist = self._session_cm.session.query(WatchList).filter(WatchList.watchlist == user.user_watchlist)
        except NoResultFound:
            pass
        return watchlist

    def add_movie_to_watchlist(self, user, movie):
        pass

    def remove_movie_from_watchlist(self, user, movie):
        pass

    def add_review(self, review: Review):
        super().add_review(review)
        with self._session_cm as scm:
            scm.session.add(review)
            scm.commit()

    def get_reviews_for_movie(self):
        reviews = self._session_cm.session.query(Review).all()
        return reviews


def movie_record_generator(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            movie_data = row
            movie_rank = movie_data[0]

            # Strip any leading/trailing white space from data read.
            movie_data = [item.strip() for item in movie_data]

            yield movie_data


def movie_actors_generator():
    article_tags_key = 0
    tag_key = 0

    for tag in tags.keys():
        tag_key = tag_key + 1
        for article_key in tags[tag]:
            article_tags_key = article_tags_key + 1
            yield article_tags_key, article_key, tag_key


def generic_generator(filename, post_process=None):
    with open(filename) as infile:
        reader = csv.reader(infile)

        # Read first line of the CSV file.
        next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]

            if post_process is not None:
                row = post_process(row)
            yield row


def process_user(user_row):
    user_row[2] = generate_password_hash(user_row[2])
    return user_row


def populate(engine: Engine, data_path: str):
    conn = engine.raw_connection()
    cursor = conn.cursor()

    insert_movies = """
        INSERT INTO movies (
        Rank, Title, Genre, Description, Director, Actors, Year, Runtime, Rating, Votes, Revenue, Metascore)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor.executemany(insert_movies, movie_actors_generator(os.path.join(data_path, 'Data1000Movies.csv')))

    insert_users = """
        INSERT INTO users (
        id, username, password)
        VALUES (?, ?, ?)"""
    cursor.executemany(insert_users, generic_generator(os.path.join(data_path, 'users.csv'), process_user))
    conn.commit()
    conn.close()
