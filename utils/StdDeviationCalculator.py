from MeanCalculator import MeanCalculator


class StdDeviationCalculator(MeanCalculator):
    def __init__(self):
        MeanCalculator.__init__(self)
        self.sum_square = 0

    def add_value(self, value):
        super().add_value(value)
        self.sum_square += value**2

    def getStdDeviation(self):
        return (self.sum_square / self.count - super().get_mean() ** 2) ** 1/2

def populate_std_calculator(list):
    std_calculator = StdDeviationCalculator()
    for number in list:
        std_calculator.add_value(number)
    return std_calculator
