from cs235flix.adapters.repository import AbstractRepository


def get_all_movies(repo: AbstractRepository):
    movies = repo.get_all_movies()
    return movies


def get_all_movies_by_rank(repo: AbstractRepository):
    movies = repo.get_all_movies_by_rank()
    return movies
