
class MeanCalculator:
    def __init__(self):
        self.sum = 0
        self.count = 0

    def add_value(self, value):
        self.sum += value
        self.count += 1

    def get_mean(self):
        return self.sum / self.count
