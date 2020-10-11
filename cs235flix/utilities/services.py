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


def get_user_watchlist(repo: AbstractRepository, user):
    watch_list = repo.get_user(user).user_watchlist.watchlist
    return watch_list


def add_movie_to_watchlist(repo: AbstractRepository, user, movie, date):
    repo.add_movie_to_watchlist(user, movie, date)


def get_user(repo: AbstractRepository, username):
    user = repo.get_user(username)
    return user


def remove_movie_from_watchlist(repo: AbstractRepository, user, movie, date):
    repo.remove_movie_from_watchlist(user, movie, date)


def add_review(repo: AbstractRepository, user, review_text, movie, date, rating):
    repo.add_review(user, review_text, movie, date, rating)


def get_reviews_for_movie(repo: AbstractRepository, movie, date):
    review_list = repo.get_reviews_for_movie(str(movie), int(date))
    return review_list
