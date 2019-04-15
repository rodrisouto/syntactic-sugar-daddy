
def median_vector(vector):
    sorted_vector = sorted(vector)
    #same as ordered vector
    return median_ordered_vector(sorted_vector)


def median_list(linked_list):
    sorted_list = sorted(linked_list)
    return median_ordered_vector(sorted_list)


def median_ordered_vector(ordered_vector):
    length = len(ordered_vector)
    if length % 2:
        return ordered_vector[length//2]
    else:
        return (ordered_vector[length//2] + ordered_vector[length//2 - 1]) // 2


def median_sorted_list(sorted_list):
    length = len(sorted_list)
    if length % 2:
        return sorted_list.get(length // 2)
    else:
        return (sorted_list.get(length // 2) + sorted_list.get(length // 2 - 1)) // 2
