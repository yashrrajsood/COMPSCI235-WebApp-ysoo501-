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


def get_list_of_genres(repo: AbstractRepository):
    g_movie_list = repo.get_genres()
    return g_movie_list


def get_genre_by_name(repo: AbstractRepository, name):
    genre = repo.get_genre_by_name(name)
    return genre


def get_movies_by_genre(repo: AbstractRepository, name):
    list_movies = repo.get_movies_by_genre(name)
    return list_movies


def get_movies_by_actor(repo: AbstractRepository, name):
    list_movies = repo.get_movies_by_actor(name)
    return list_movies


def get_list_of_actors(repo: AbstractRepository):
    list_actors = repo.get_actors()
    return list_actors


def get_list_of_directors(repo: AbstractRepository):
    list_directors = repo.get_directors()
    return list_directors


def get_movies_by_director(repo: AbstractRepository, name):
    list_movies = repo.get_movies_by_director(name)
    return list_movies
