from typing import Dict

from city import City

class Empire:
    _player: int
    _metropolis: str
    _original_troops_at_loading: Dict[str, int]

    def __init__(self, player, metropolis, placed_troops):
        self._player = player
        self._metropolis = metropolis
        self._original_troops_at_loading = placed_troops

    def __str__(self):
        return '<Empire: ({}, metropolis={}, _original_troops_at_loading={}>'.format(self._player, self._metropolis,
                                                                                     self._original_troops_at_loading)

    def __repr__(self):
        return '<Empire: ({}, metropolis={}, _original_troops_at_loading={}>'.format(self._player, self._metropolis,
                                                                                     self._original_troops_at_loading)

    def get_player(self):
        return self._player

    def get_metropolis(self):
        return self._metropolis

    def get_original_troops_at_loading(self):
        return self._original_troops_at_loading
