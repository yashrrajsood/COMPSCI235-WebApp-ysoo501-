import csv
import os

from cs235flix.adapters.repository import AbstractRepository, RepositoryException
from cs235flix.domain.model import User, Actor, Genre, Movie, Director

from werkzeug.security import generate_password_hash

class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._movies = list()
        self._users = list()
        self._genres = list()
        self._directors = set(list())
        self._actors = set(list())

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user._username == username), None)

    def add_movie(self, movie: Movie):
        self._movies += [movie]

    def get_all_movies(self):
        return self._movies

    def add_genre(self, genre: Genre):
        self._genres += [genre]

    def get_genres(self):
        return sorted(self._genres)

    def get_directors(self):
        return self._directors

    def add_director(self, director: Director):
        self._directors.add(director)

    def add_actor(self, actor: Actor):
        self._actors.add(actor)

    def get_actors(self):
        return self._actors

    def get_all_movies_by_rank(self):
        temp = sorted(self._movies, key=lambda x: x.rank)
        return temp

    def get_movie_by_name(self, title, date):
        temp_movie = Movie(None, title, date, None, None, None, None, None, None)
        if temp_movie in self._movies:
            return self._movies[self._movies.index(temp_movie)]
        else:
            return None

    def get_genre_by_name(self, name):
        for genre in self._genres:
            if genre.genre_name == name:
                return genre

    def get_movies_by_genre(self, genre_name):
        temp = []
        temp_genre = Genre(genre_name)
        for movie in self._movies:
            if temp_genre in movie.genres:
                temp += [movie]
        return temp

    def get_movies_by_actor(self, name):
        temp = []
        temp_actor = Actor(name)
        for movie in self._movies:
            if temp_actor in movie._actors:
                temp += [movie]
        return temp

    def get_movies_by_director(self, name):
        temp = []
        temp_director = Director(name)
        for movie in self._movies:
            if temp_director == movie.director:
                temp += [movie]
        return temp

    def get_user_watchlist(self, user):
        for users in self._users:
            if user == users.user_name:
                return users.user_watchlist
            else:
                return None


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_movies(data_path: str, repo: MemoryRepository):
    for data_row in read_csv_file(os.path.join(data_path, 'Data1000Movies.csv')):

        # Movie Object Creation
        temp_rank = data_row[0]
        temp_title = data_row[1]
        temp_release_date = data_row[6]
        temp_description = data_row[3]
        temp_run_time = data_row[7]
        temp_rating = data_row[8]
        temp_votes = data_row[9]
        temp_revenue = data_row[10]
        temp_metascore = data_row[11]
        movie = Movie(temp_rank, temp_title, temp_release_date, temp_description, temp_run_time, temp_rating,
                      temp_votes, temp_revenue, temp_metascore)

        # Director Creation
        director = Director(str(data_row[4]))
        movie.director = director
        if director not in repo.get_directors():
            repo.add_director(director)

        # Genres Creation
        genres = data_row[2]
        genre_list = genres.split(",")
        for g in genre_list:
            new_genre = Genre(g.strip())
            if new_genre not in repo.get_genres():
                repo.add_genre(new_genre)
            movie.add_genre(new_genre)

        # Actors Creation
        actors = data_row[5]
        actors_list = actors.split(",")
        for a in actors_list:
            new_actor = Actor(a.strip())
            if new_actor not in repo.get_actors():
                repo.add_actor(new_actor)
            movie.add_actor(new_actor)

        repo.add_movie(movie)

def load_users(data_path: str, repo: MemoryRepository):
    users = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(
            username=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)
        users[data_row[0]] = user
    return users


def populate(data_path: str, repo: MemoryRepository):
    # Loading all movies, directors and actors
    load_movies(data_path, repo)
    load_users(data_path, repo)
    users = load_users(data_path, repo)

