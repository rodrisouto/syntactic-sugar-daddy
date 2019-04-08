def median_vector(vector):
    sorted_vector = sorted(vector)
    #same as ordered vector
    return median_ordered_vector(sorted_vector)


def median_ordered_vector(ordered_vector):
    length = len(ordered_vector)
    if length % 2:
        return ordered_vector[length//2]
    else:
        return (ordered_vector[length//2] + ordered_vector[length//2 - 1]) // 2
