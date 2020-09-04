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
