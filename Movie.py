from Director import Director
from Actor import Actor
from Genre import Genre


class Movie:
    def __init__(self, title: str, release_date: int):
        self.title = title

        if release_date >= 1900 and isinstance(release_date, int):
            self._release_date = release_date

        self._actors = []
        self._genres = []

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title):
        if title != "" and isinstance(title, str):
            self._title = title.strip()
        else:
            self._title = None

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description):
        if description != "" and isinstance(description, str):
            self._description = description.strip()
        else:
            self._description = None

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, director):
        if isinstance(director, Director):
            self._director = director

    @property
    def actors(self):
        return self._actors

    @actors.setter
    def actors(self, val):
        if isinstance(val, list):
            self._actors = val

    @property
    def genres(self):
        return self._genres

    @genres.setter
    def genres(self, val):
        if isinstance(val, list):
            self._genres = val

    @property
    def runtime_minutes(self) -> int:
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if runtime_minutes >= 0:
            self._runtime_minutes = runtime_minutes
        else:
            raise ValueError()

    def __repr__(self) -> str:
        return f'<Movie {self._title}, {self._release_date}>'

    def __eq__(self, other_movie) -> bool:
        if not isinstance(other_movie, Movie):
            return False
        return other_movie._title == self._title and other_movie._release_date == self._release_date

    def __lt__(self, other_movie):
        #return self._title < other_movie._title and self._release_date < other_movie._release_date
        return (self._title, self._release_date) < (other_movie._title, other_movie._release_date)

    def __hash__(self):
        return hash(str((self._title + " " + str(self._release_date))))

    def add_actor(self, actor):
        if isinstance(actor, Actor):
            self._actors += [actor]
        #actor.add_actor_colleague(self)

    def remove_actor(self, actor):
        if actor in self._actors:
            self._actors.remove(actor)

    def add_genre(self, genre):
        if isinstance(genre, Genre):
            self._genres += [genre]

    def remove_genre(self, genre):
        if genre in self._genres:
            self._genres.remove(genre)

""""
movie = Movie("Test", 2013)
print(hash(movie))

movie2 = Movie("Test", 2013)
print(hash(movie2))

movie.runtime_minutes = 44
print("Movie runtime: {} minutes".format(movie.runtime_minutes))

director3 = Director("Name Name")
movie.director = director3
print(movie.director)

actor = Actor("David")
actor2 = Actor("Sam")
movie.add_actor(actor)
movie.add_actor(actor2)
movie.add_actor(director3)
print(movie.actors)

genre = Genre("Action")
genre2 = Genre("Comedy")
movie.add_genre(genre)
movie.add_genre(genre2)
movie.add_genre(director3)
print(movie.genres)
"""
