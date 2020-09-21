from flask import Blueprint

import cs235flix.adapters.repository as repo
import cs235flix.utilities.services as services

# Configure Blueprint.
utilities_blueprint = Blueprint(
    'utilities_bp', __name__)


def get_movies():
    movies = services.get_all_movies(repo.repo_instance)
    return movies


def get_movies_by_rank():
    movies = services.get_all_movies_by_rank(repo.repo_instance)
    return movies


def get_movie_from_title(title, date):
    movie = services.get_movie_from_name(repo.repo_instance, title, date)
    return movie


def get_list_of_genres():
    genre_list = services.get_list_of_genres(repo.repo_instance)
    return genre_list


def get_genre_by_name(name):
    genre = services.get_genre_by_name(repo.repo_instance, name)
    return genre


def get_movies_by_genre(name):
    list_movies = services.get_movies_by_genre(repo.repo_instance, name)
    return list_movies


def get_movies_by_actor(name):
    list_movies = services.get_movies_by_actor(repo.repo_instance, name)
    return list_movies


def get_list_of_actors():
    list_actors = services.get_list_of_actors(repo.repo_instance)
    return list_actors


def get_list_of_directors():
    list_directors = services.get_list_of_directors(repo.repo_instance)
    return list_directors


def get_movies_by_director(name):
    list_movies = services.get_movies_by_director(repo.repo_instance, name)
    return list_movies
