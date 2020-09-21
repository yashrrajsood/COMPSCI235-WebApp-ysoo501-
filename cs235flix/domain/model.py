from datetime import datetime


class User:
    def __init__(self, user_name, password):
        self._user_name = user_name.strip().lower()
        self._password = password
        self._watched_movies = []
        self._reviews = []
        self._time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self._user_name

    @property
    def password(self):
        return self._password

    @property
    def watched_movies(self):
        return self._watched_movies

    @property
    def reviews(self):
        return self._reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self._time_spent_watching_movies_minutes

    def __repr__(self) -> str:
        return f'<User {self._user_name}>'

    def __eq__(self, other_user) -> bool:
        if not isinstance(other_user, User):
            return False
        return other_user._user_name == self._user_name

    def __lt__(self, other_user):
        return self._user_name < other_user._user_name

    def __hash__(self):
        return hash(self._user_name)

    def watch_movie(self, movie):
        if movie not in self._watched_movies:
            self._watched_movies += [movie]
            self._time_spent_watching_movies_minutes += movie._runtime_minutes

    def add_review(self, review):
        if review not in self._reviews:
            self._reviews += [review]


class Actor:
    def __init__(self, name: str):
        if name != "" and isinstance(name, str):
            self._name: str = name
        else:
            self._name = None
        self._colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f'<Actor {self._name}>'

    def __eq__(self, other_actor) -> bool:
        if not isinstance(other_actor, Actor):
            return False
        return other_actor._name == self._name

    def __lt__(self, other_actor):
        return self._name < other_actor._name

    def __hash__(self):
        return hash(self._name)

    def add_actor_colleague(self, colleague):
        if colleague not in self._colleagues:
            self._colleagues += [colleague]

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self._colleagues:
            return True
        else:
            return False


class Genre:
    def __init__(self, name: str):
        if name != "":
            self._name: str = name
        else:
            self._name = None

        self._movie_list = []

    @property
    def genre_name(self) -> str:
        return self._name

    @property
    def movie_list(self):
        return self._movie_list

    def add_movie(self, movie):
        if movie not in self._movie_list:
            self._movie_list.append(movie)

    def __repr__(self) -> str:
        return f'<Genre {self._name}>'

    def __eq__(self, other_genre) -> bool:
        if not isinstance(other_genre, Genre):
            return False
        return other_genre._name == self._name

    def __lt__(self, other_genre):
        return self._name < other_genre._name

    def __hash__(self):
        return hash(self._name)


class Review:
    def __init__(self, movie, review_text: str, rating: int):
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


class Movie:
    def __init__(self, rank, title, release_date, description, run_time, rating, votes, revenue, metascore):
        self.title = title
        release_date = int(release_date)
        if release_date >= 1900 and isinstance(release_date, int):
            self._release_date = release_date

        self._actors = []
        self._genres = []
        self._description = description
        self._runtime_minutes = run_time
        self._rating = rating
        self._votes = votes
        self._revenue = revenue
        self._metascore = metascore
        self._director = None
        self._rank = rank

    @property
    def rank(self) -> int:
        return self._rank

    @rank.setter
    def rank(self, rank):
        if isinstance(rank, int):
            self._rank = int(rank)
        else:
            self._rank = None

    @property
    def rating(self) -> float:
        return self._rating

    @rating.setter
    def rating(self, rating):
        if 10 >= rating >= 0:
            self._rating = float(rating)
        else:
            self._rating = None

    @property
    def release_date(self):
        return self._release_date

    @property
    def votes(self) -> int:
        return self._votes

    @votes.setter
    def votes(self, votes):
        if isinstance(votes, int):
            self._votes = int(votes)
        else:
            self._votes = None

    @property
    def revenue(self):
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        if isinstance(revenue, int) or isinstance(revenue, float):
            self._revenue = float(revenue)
        else:
            self._revenue = None

    @property
    def metascore(self):
        return self._metascore

    @metascore.setter
    def metascore(self, metascore):
        if isinstance(metascore, int):
            self._metascore = int(metascore)
        else:
            self._metascore = None

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
    '''
    @genres.setter
    def genres(self, val):
        if isinstance(val, list):
            self._genres = val
    '''

    @property
    def runtime_minutes(self) -> int:
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if runtime_minutes >= 0:
            self._runtime_minutes = int(runtime_minutes)
        else:
            raise ValueError()

    def __repr__(self) -> str:
        return f'<Movie {self._title}, {self._release_date}>'

    def __eq__(self, other_movie) -> bool:
        if not isinstance(other_movie, Movie):
            return False
        return other_movie._title == self._title and other_movie._release_date == self._release_date

    def __lt__(self, other_movie):
        return (self._title, self._release_date) < (other_movie._title, other_movie._release_date)

    def __hash__(self):
        return hash(str((self._title + " " + str(self._release_date))))

    def add_actor(self, actor):
        if isinstance(actor, Actor):
            self._actors += [actor]
        # actor.add_actor_colleague(self)

    def remove_actor(self, actor):
        if actor in self._actors:
            self._actors.remove(actor)

    def add_genre(self, genre):
        if isinstance(genre, Genre):
            self._genres += [genre]

    def remove_genre(self, genre):
        if genre in self._genres:
            self._genres.remove(genre)


class Director:
    def __init__(self, name: str):
        if name != "":
            self._name: str = name
        else:
            self._name = None

    @property
    def director_full_name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f'<Director {self._name}>'

    def __eq__(self, other_director) -> bool:
        if not isinstance(other_director, Director):
            return False
        return other_director._name == self._name

    def __lt__(self, other_director):
        return self._name < other_director._name

    def __hash__(self):
        return hash(self._name)


class WatchList:
    def __init__(self):
        self._watch_list = []

    def add_movie(self, movie):
        if movie not in self._watch_list and isinstance(movie, Movie):
            self._watch_list += [movie]

    def remove_movie(self, movie):
        if movie in self._watch_list:
            self._watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if index in range(len(self._watch_list)):
            return self._watch_list[index]
        else:
            return None

    def size(self):
        return len(self._watch_list)

    def first_movie_in_watchlist(self):
        if len(self._watch_list) > 0:
            return self._watch_list[0]
        else:
            return None

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= len(self._watch_list):
            c = self.n
            self.n += 1
            return c
        else:
            raise StopIteration


class PartyRoom:
    def __init__(self, name, host, movie):
        self._party_name = name
        self._host = host
        self._current_movie = movie
        self.watched_movies = []
        self.users_watching = [host]

    def change_host(self, new_host):
        if isinstance(new_host, User) and new_host in self.users_watching:
            self._host = new_host

    def change_movie(self, new_movie):
        if isinstance(new_movie, Movie):
            self.watched_movies += [self._current_movie]
            self._current_movie = new_movie

    def add_user(self, new_user):
        if isinstance(new_user, User) and new_user not in self.users_watching:
            self.users_watching += [new_user]

    def remove_user(self, person):
        if person in self.users_watching and person != self._host:
            self.users_watching.remove(person)

    def show_history(self):
        return self.watched_movies

    def change_party_name(self, new_name):
        if new_name != "":
            self._party_name = new_name

    def __repr__(self):
        return f'<PartyRoom "{self._party_name}" watching {self._current_movie}, with user(s) {self.users_watching}>'


class ModelException(Exception):
    pass


'''
temp = Movie(1, "Guardians of the Galaxy", 2014, None, None, None, None, None, None)
temp2 = Movie(2, "Sing", 2016, None, None, None, None, None, None)
temp3= Movie(8, "Mindhorn", 2016, None, None, None, None, None, None)

all_movies = [temp, temp2, temp3]

to_find = Movie(2, "Guardians of the Galaxy", 2014, "Lmao", 100, 30, 30000, 200, 10)
if to_find in all_movies:
    print(all_movies[all_movies.index(to_find)])
'''
