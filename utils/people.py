class Person:

    def __init__(self, name):
        self.partners = []
        self.preferences = None
        self.name = name
        self.positions = {}

    def __repr__(self):
        return '( Person: ' + self.name + ' | ' + str(len(self.preferences)) + ' )'

    def set_preferences(self, people):
        self.preferences = people
        for i in range(len(people)):
            for j in range(len(people[i])):
                self.positions[people[i][j]] = (i, j)

    def engage(self, person):
        self.partners.append(person)

    def get_preferred(self):
        if len(self.preferences):
            return self.preferences[0]

    def pop_preferred(self):
        if len(self.preferences):
            return self.preferences.pop(0)

    def is_free(self):
        return not len(self.partners)

    def get_rejected(self, person):
        preference = self.positions[person][0]
        rejected = []
        for i in self.partners:
            if self.positions[i][0] < preference:
                rejected.append(i)
                self.partners.remove(i)
        return rejected

    def is_multiply_engaged(self):
        return len(self.partners) > 1

    def get_partners(self):
        return self.partners

    def free(self, partner):
        self.partners.remove(partner)
