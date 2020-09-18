from cs235flix.adapters.repository import AbstractRepository


def get_all_movies(repo: AbstractRepository):
    movies = repo.get_all_movies()
    return movies


def get_all_movies_by_rank(repo: AbstractRepository):
    movies = repo.get_all_movies_by_rank()
    return movies


def get_movie_from_name(repo: AbstractRepository, title, date):
    movie = repo.get_movie_by_name(title, date)
    return movie

