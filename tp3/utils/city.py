
class City:
    _name: str
    _spices: int
    _owner: int
    _troops: int

    def __init__(self, name, spices):
        self._name = name
        self._spices = spices
        self._owner = None
        self._troops = 0

    def __str__(self):
        return '<City: ({}, spices={}, owner={}, troops={})>'.format(self._name, self._spices, self._owner,
                                                                     self._troops)

    def __repr__(self):
        return '<City: ({}, spices={}, owner={}, troops={})>'.format(self._name, self._spices, self._owner,
                                                                     self._troops)

    def get_name(self):
        return self._name

    def get_spices(self):
        return self._spices

    def get_owner(self):
        return self._owner

    def get_troops(self):
        return self._troops

    def assign_owner(self, owner, troops):
        assert owner is not None
        assert troops > 0

        self._owner = owner
        self._troops = troops

    def discount_troops(self, troops_to_discount):
        assert self._owner is not None, 'City {} has no owner.'.format(self)
        assert self._troops >= troops_to_discount, '{} {}'.format(self._troops, troops_to_discount)

        self._troops -= troops_to_discount

    def receive_attack(self, attacker, attacking_troops):
        # assert attacker is not self._owner, 'Can not attack one self. {}'.format(attacker, self)

        self._troops -= attacking_troops

        if self._troops == 0:
            self._owner = None
        elif self._troops < 0:
            self._troops *= -1
            self._owner = attacker

    def free_if_troopless(self):
        if self._troops == 0:
            self._owner = None

    def place_troops(self, spice):
        self._troops += spice * 2
