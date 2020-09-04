from Movie import Movie

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


