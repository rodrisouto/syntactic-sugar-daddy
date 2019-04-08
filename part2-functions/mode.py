def mode_vector(vector):
    appearances = {}
    for i in range(len(vector)):
        if not vector[i] in appearances:
            appearances[vector[i]] = 0
        appearances[vector[i]] += 1

    max = sorted(appearances.values())[-1]
    if max == 1:
        return []

    numbers = []
    for element in appearances.items():
        if element[1] == max:
            numbers.append(element[0])
    return numbers


def mode_ordered_vector(ordered_vector):
    return mode_vector(ordered_vector)






