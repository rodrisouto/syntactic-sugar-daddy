from mean import mean_vector
from mean import mean_list


def standard_deviation_vector(vector):
    mean = mean_vector(vector)
    deviation = 0
    for i in range(len(vector)):
        deviation += (vector[i] - mean) ** 2
    return (deviation / len(vector)) ** (1/2)


def standard_deviation_list(linked_list):
    mean = mean_list(linked_list)
    deviation = 0
    for n in linked_list:
        deviation += (n - mean) ** 2
    return (deviation / len(linked_list)) ** (1/2)


def standard_deviation_ordered_vector(ordered_vector):
    return standard_deviation_vector(ordered_vector)


def standard_deviation_STD_calculator(std_calculator):
    return std_calculator.getStdDeviation()