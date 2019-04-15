def permutations_vector(vector):
    length = len(vector)
    copy = vector.copy()
    out = []
    permutations(copy, 0, length, out)
    print(out)


def permutations(vector, partial, length, out):
    if partial == length:
        copy = vector.copy()
        out.append(copy)
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
    return permutations_vector(sorted_list)

# TODO: our structure(done?)
