class Genre:
    def __init__(self, name: str):
        if name != "":
            self._name: str = name
        else:
            self._name = None

    @property
    def genre_name(self) -> str:
        return self._name

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