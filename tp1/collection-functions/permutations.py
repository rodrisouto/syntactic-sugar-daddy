def permutations_vector(vector):
    length = len(vector)
    copy = vector.copy()
    out = []
    permutations(copy, 0, length, out)
    return out


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
    # copy list to vector (O(n))
    permutations_vector(linked_list)


def permutations_ordered_vector(ordered_vector):
    #same
    return permutations_vector(ordered_vector)

# TODO: our structure
