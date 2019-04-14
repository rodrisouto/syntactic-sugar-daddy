class Person:

    def __init__(self, name):
        self.partner = None
        self.preferences = None
        self.name = name

    def __repr__(self):
        return self.name

    def set_preferences(self, people):
        self.preferences = people

    def get_preferred(self):
        return self.preferences.pop(0)

    def is_free(self):
        return not self.partner

    def engage(self, other_person):
        self.partner = other_person

    def prefers(self, other_person):
        i1 = self.preferences.index(other_person)
        i2 = self.preferences.index(self.partner)
        value = True if (i1 < i2) else False
        return value

    def can_propose(self):
        return len(self.preferences) and not self.partner

    def get_partner(self):
        return self.partner

    def release(self):
        aux = self.partner
        self.partner = None
        return aux


