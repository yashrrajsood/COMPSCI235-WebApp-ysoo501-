from Movie import Movie
from Actor import Actor
from Director import Director
from Genre import Genre
from datetime import datetime


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        self._movie = movie
        self._review_text = review_text
        if 0 < rating < 10:
            self._rating = rating
        else:
            self._rating = None
        self._timestamp = datetime.datetime.now()

    @property
    def movie(self):
        return self._movie

    @property
    def review_text(self):
        return self._review_text

    @property
    def rating(self):
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp

    def __repr__(self) -> str:
        return f'<Movie {self._movie._title}, {self._movie._release_date}>'

    def __eq__(self, other_review) -> bool:
        if not isinstance(other_review, Review):
            return False
        return other_review._movie == self._movie and other_review._review_text == self._review_text and other_review._rating == self._rating and other_review._timestamp == self._timestamp
