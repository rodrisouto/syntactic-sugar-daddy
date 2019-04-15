
def variations_with_repetitions_vector(vector, r):
    if r == 1:
        return [[x] for x in vector]
    vars = []
    for i in range(len(vector)):
        element = vector[i]
        smaller_vars = variations_with_repetitions_vector(vector[i:], r - 1)
        for j in range(len(smaller_vars)):
            vars.append([element] + smaller_vars[j])
    return vars


def variations_with_repetition_list(linked_list, r):
    if r == 1:
        return [[x] for x in linked_list]
    vars = []
    i = 0
    for element in linked_list:
        smaller_vars = variations_with_repetitions_vector(linked_list[i:], r - 1)
        for smaller_var in smaller_vars:
            vars.append([element] + smaller_var)
        i += 1
    return vars


def variations_with_ordered_vector(ordered_vector, r):
    return variations_with_repetitions_vector(ordered_vector, r)

# TODO: our structure
