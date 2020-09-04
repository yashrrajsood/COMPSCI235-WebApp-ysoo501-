from User import User
from Movie import Movie

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

partyroom = PartyRoom("Friends from school!", User("Yashsood", "Doesntmatter"), Movie("A", 2015))
partyroom.add_user(User("Max", "deos"))
print(partyroom)

