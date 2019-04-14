
class MeanCalculator:
    def __init__(self):
        self.sum = 0
        self.count = 0

    def add_value(self, value):
        self.sum += value
        self.count += 1

    def get_mean(self):
        return self.sum / self.count


def populate_mean_calculator(vector):
    calculator = MeanCalculator()
    for element in vector:
        calculator.add_value(element)
    return calculator
