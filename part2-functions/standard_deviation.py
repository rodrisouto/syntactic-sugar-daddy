from mean import mean_vector


def standard_deviation_vector(vector):
    mean = mean_vector(vector)
    deviation = 0
    for i in range(len(vector)):
        deviation += (vector[i] - mean)**2
    return (deviation/len(vector))**1/2


def standard_deviation_ordered_vector(ordered_vector):
    return standard_deviation_vector(ordered_vector)


standard_deviation_vector([2, 4, 4, 4, 5, 5, 7, 9])


