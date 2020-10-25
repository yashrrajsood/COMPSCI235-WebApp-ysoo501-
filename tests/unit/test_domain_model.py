from datetime import date

from cs235flix.domain.model import User, Movie

import pytest


@pytest.fixture()
def user():
    return User('dbowie', '1234567890')


def test_user_construction(user):
    assert user.username == 'dbowie'
    assert user.password == '1234567890'
    assert repr(user) == '<User dbowie 1234567890>'

    for review in user.reviews:
        # User should have an empty list of Movie Reviews after construction.
        assert False


def test_movie_construction(movie):
    assert movie.title == 'Yash Test Movie'
    assert movie.release_date == 2020
    assert movie.rank == 10000
    assert movie.description == 'The test movie object created by Yash Sood'
    assert movie.runtime_minutes == 200
    assert movie.rating == 10
    assert movie.votes == 10
    assert movie.revenue == 100
    assert movie.metascore == 10

    assert repr(movie) == '<(Movie) Yash test Movie 2000>'


def test_movie_less_than_operator():
    movie_1 = Movie(1, "Guardians of the Galaxy", 2014, None, None, None, None, None, None)

    movie_2 = Movie(2, "Sing", 2016, None, None, None, None, None, None)

    assert movie_1 < movie_2
