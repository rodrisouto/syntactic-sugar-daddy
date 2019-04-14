class Person:

    def __init__(self, name):
        self.partner = None
        self.preferences = None
        self.name = name

    def __repr__(self):
        return self.name

    def set_preferences(self, people):
        self.preferences = people

    def engage(self, person):
        self.partner = person

    def get_preferred(self):
        if len(self.preferences):
            return self.preferences[0]

    def is_free(self):
        return not self.partner

    def prefers(self, person):
        index1 = self.preferences.index(person)
        index2 = self.preferences.index(self.partner)
        value = True if (index1 < index2) else False
        return value

    def release(self):
        ex = self.partner
        self.partner = None
        return ex

    def free(self):
        self.partner = None
