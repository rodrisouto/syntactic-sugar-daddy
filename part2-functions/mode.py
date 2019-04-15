def mode_vector(vector):
    appearances = dict()
    for i in range(len(vector)):
        element = vector[i]
        appearances[element] = appearances.get(element, 0) + 1
    mode = set()
    max = vector[0]
    for k, v in appearances.items():
        if v > max:
            mode = {k}
            max = v
        if v == max:
            mode.add(k)
    return mode


def mode_list(linked_list):
    appearances = dict()
    for element in linked_list:
        appearances[element] = appearances.get(element, 0) + 1
    mode = set()
    max = linked_list[0]
    for k, v in appearances.items():
        if v > max:
            mode = {k}
            max = v
        elif v == max:
            mode.add(k)
    return mode


def mode_ordered_vector(ordered_vector):
    mode = set()
    max_count = 0
    count = 0
    last_number = ordered_vector[0]
    for i in range(1, len(ordered_vector)):
        number = ordered_vector[i]
        if last_number == number:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            mode = {number}
        elif count == max_count:
            mode.add(number)
        last_number = number
    return mode


def mode_sorted_list(sorted_list):
    mode = set()
    max_count = 0
    count = 0
    last_number = sorted_list.get(0)
    for number in sorted_list:
        if last_number == number:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            mode = {number}
        elif count == max_count:
            mode.add(number)
        last_number = number
    return mode
