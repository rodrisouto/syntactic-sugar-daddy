class Man:
    def __init__(self, women):
        self.partner = None
        self.preferences = women

    def engage(self, woman):
        self.partner = woman

    def get_prefered(self):
        return self.preferences.pop()

    def free(self):
        self.partner = None


class Woman:
    def __init__(self, men):
        self.partner = None
        self.preferences = men

    def engage(self, man):
        self.partner = man

    def prefers(self, man):
        #compare

    def release(self):
        ex = self.partner
        self.partner = None
        return ex