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
        return (self._user_name) < (other_user._user_name)

    def __hash__(self):
        return hash(self._user_name)

    def watch_movie(self, movie):
        if movie not in self._watched_movies:
            self._watched_movies += [movie]
            self._time_spent_watching_movies_minutes += movie._runtime_minutes

    def add_review(self, review):
        if review not in self._reviews:
            self._reviews += [review]

