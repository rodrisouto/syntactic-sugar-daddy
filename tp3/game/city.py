
class City:
    _name: str
    _spices: int

    def __init__(self, name, spices):
        self._name = name
        self._spices = spices

    def __str__(self):
        return 'City: ({}, {})'.format(self._name, self._spices)

    def __repr__(self):
        # !!!!
        # return 'C_{}'.format(self._name)
        return str(self._name)

    def get_name(self):
        return self._name

    def get_spices(self):
        return self._spices