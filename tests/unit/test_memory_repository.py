from cs235flix.domain.model import User, Movie
import pytest


def test_repository_can_add_a_user(in_memory_repo):
    user = User('Dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('Dave') is user


def test_repository_can_retrieve_a_user(in_memory_repo):
    user = in_memory_repo.get_user('fmercury')
    assert user == User('fmercury', '8734gfe2058v')


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None


def test_repository_can_add_movie(in_memory_repo):
    movie = Movie(Movie(1, "Guardians of the Galaxy", 2014, None, None, None, None, None, None))
    in_memory_repo.add_movie(movie)

    assert movie in in_memory_repo.get_all_movies()


def test_repository_can_retrieve_movie(in_memory_repo):
    movie = in_memory_repo.get_all_movies(0)

    # Check that the Movie has the expected title.
    assert movie.title == 'Guardians of the Galaxy'


def test_repository_does_not_retrieve_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_all_movies(10199)
    assert movie is None


def test_repository_can_retrieve_movies_by_rank(in_memory_repo):
    movies = in_memory_repo.get_all_movies_by_rank()

    # Check that the query returned 1000 movies.
    assert len(movies) == 1000


def test_repository_can_retrieve_movies_by_title(in_memory_repo):
    movie = in_memory_repo.get_movie_by_name('Guardians of the Galaxy', 2014)
    assert movie is not None


def test_repository_can_retrieve_movies_by_genre(in_memory_repo):
    movies = in_memory_repo.get_movies_by_genre('Comedy')
    assert movies[0].genre.genre_name == 'Comedy'


def test_repository_can_retrieve_movies_by_actor(in_memory_repo):
    movies = in_memory_repo.get_movies_by_actor('Chris Pratt')
    assert movies[0]._actors[0].actor_full_name == 'Chris Pratt'


def test_repository_can_retrieve_movies_by_director(in_memory_repo):
    movies = in_memory_repo.get_movies_by_director('James Gunn')
    assert movies[0].director._name == 'James Gunn'