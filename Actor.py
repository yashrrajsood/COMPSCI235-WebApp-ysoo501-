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

