class Person:

    def __init__(self, name):
        self.partner = None
        self.preferences = None
        self.name = name
        self.positions = {}

    def __repr__(self):
        return '( Person2: ' + self.name + ' | ' + str(len(self.preferences)) + ' )'

    def set_preferences(self, people):
        for i in range(len(people)):
            self.positions[people[i]] = i
        self.preferences = people[::-1]

    def get_preferred(self):
        return self.preferences[-1]

    def pop_preferred(self):
        return self.preferences.pop()

    def is_free(self):
        return not self.partner

    def engage(self, other_person):
        self.partner = other_person

    def prefers(self, other_person):
        i1 = self.positions[other_person]
        i2 = self.positions[self.partner]
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


