from MeanCalculator import MeanCalculator


def mean_vector(vector):
    sum = 0
    for i in range(len(vector)):
        sum += vector[i]
    return sum / len(vector)


def mean_list(linked_list):
    sum = 0
    count = 0
    for n in linked_list:
        sum += n
        count += 1
    return sum / count


def mean_ordered_vector(ordered_vector):
    # same as any vector
    return mean_vector(ordered_vector)


def mean_calculator(mean_calculator):
    return mean_calculator.get_mean()


def populate_mean_calculator(vector):
    calculator = MeanCalculator()
    for element in vector:
        calculator.add_value(element)
    return calculator
