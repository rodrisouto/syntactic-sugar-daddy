from typing import Dict


class Empire:
    _player: int
    _metropolis: str
    _placed_troops: Dict[str, int]

    def __init__(self, player, metropolis, placed_troops):
        self._player = player
        self._metropolis = metropolis
        self._placed_troops = placed_troops

    def __str__(self):
        return '<Empire: ({}, metropolis={}, placed_troops={}>'.format(self._player, self._metropolis,
                                                                       self._placed_troops)

    def __repr__(self):
        return '<Empire: ({}, metropolis={}, placed_troops={}>'.format(self._player, self._metropolis,
                                                                       self._placed_troops)

    def get_player(self):
        return self._player

    def get_metropolis(self):
        return self._metropolis

    def get_placed_troops(self):
        return self._placed_troops
