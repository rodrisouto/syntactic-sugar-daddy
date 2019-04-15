
def variations_vector(vector, r):
    if r == 1:
        return [[x] for x in vector]
    vars = []
    for i in range(len(vector)):
        element = vector[i]
        smaller_vars = variations_vector(vector[i + 1:], r - 1)
        for j in range(len(smaller_vars)):
            vars.append([element] + smaller_vars[j])
    return vars


def variations_list(linked_list, r):
    if r == 1:
        return [[x] for x in linked_list]
    vars = []
    i = 0
    for element in linked_list:
        smaller_vars = variations_list(linked_list[i + 1:], r - 1)
        for smaller_var in smaller_vars:
            vars.append([element] + smaller_var)
        i += 1
    return vars


def variations_ordered_vector(ordered_vector, r):
    return variations_vector(ordered_vector, r)


def variations_sorted_list(sorted_list, r):
    return variations_vector(sorted_list, r)

# TODO: our structure(done?)
