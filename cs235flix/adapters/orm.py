from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey, Float
)
from sqlalchemy.orm import mapper, relationship

from cs235flix.domain import model

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False)
)

reviews = Table(
    'reviews', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', ForeignKey('users.id')),
    Column('movie_id', ForeignKey('movies.id')),
    Column('review_text', String(1024), nullable=False),
    Column('timestamp', DateTime, nullable=False)
)

movies = Table(
    'movies', metadata,
    Column('rank', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255), nullable=False),
    Column('date', Date, nullable=False),
    Column('description', String(1024), nullable=False),
    Column('runtime', Integer, nullable=False),
    Column('rating', Float, nullable=False),
    Column('votes', Integer, nullable=False),
    Column('revenue', Float, nullable=False),
    Column('metascore', Integer, nullable=False),
    Column('director', String(255)),
    Column('actors', String(1024)),
    Column('genres', String(1024))
)

movie_actors = Table(
    'movie_actors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('movie_id', ForeignKey('movies.rank')),
    Column('actor_id', ForeignKey('actors.id')),
)

movie_genres = Table(
    'movie_genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('movie_id', ForeignKey('movies.rank')),
    Column('genre_id', ForeignKey('genres.id'))
)


genres = Table(
    'genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255))
)

actors = Table(
    'actors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255))
)

watchlist = Table(
    'watchlist', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', ForeignKey('users.id')),
    Column('movie_id', ForeignKey('movies.rank'))
)


def map_model_to_tables():
    mapper(model.User, users, properties={
        '_username': users.c.username,
        '_password': users.c.password,
        '_reviews': relationship(model.Review, backref='_user')
    })
    mapper(model.Review, reviews, properties={
        '_review_text': reviews.c.review_text,
        '_timestamp': reviews.c.timestamp
    })

    movies_mapper = mapper(model.Movie, movies, properties={
        '_rank': movies.c.rank,
        'title': movies.c.title,
        'release_date': movies.c.date,
        '_description': movies.c.description,
        '_runtime_minutes': movies.c.runtime,
        '_rating': movies.c.rating,
        '_votes': movies.c.votes,
        '_revenue': movies.c.revenue,
        '_metascore': movies.c.metascore,
        '_director': movies.c.director,
        '_reviews': relationship(model.Review, backref='_movie')
    })

    mapper(model.Actor, actors, properties={
        '_name': actors.c.name
    })
