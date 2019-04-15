def permutations_vector(vector):
    length = len(vector)
    out = []
    permutations(vector, 0, length, out)
    return out


def permutations(vector, partial, length, out):
    if partial == length:
        out.append(vector[:])
    else:
        for i in range(partial, length):
            vector[partial], vector[i] = vector[i], vector[partial]
            permutations(vector, partial + 1, length, out)
            vector[partial], vector[i] = vector[i], vector[partial]


def permutations_list(linked_list):
    return permutations_vector(linked_list)


def permutations_ordered_vector(ordered_vector):
    return permutations_vector(ordered_vector)


def permutations_sorted_list(sorted_list):
    vector = []
    for element in sorted_list:
        vector.append(element)
    return permutations_vector(vector)
