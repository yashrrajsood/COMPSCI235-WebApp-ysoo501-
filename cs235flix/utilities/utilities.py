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
