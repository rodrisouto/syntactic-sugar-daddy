import heapq


def max_vector(vector):
    max_n = vector[0]
    for i in range(1, len(vector)):
        if vector[i] > max_n:
            max_n = vector[i]
    return max_n


def max_list(linked_list):
    max_n = linked_list[0]
    for n in linked_list:
        if n > max_n:
            max_n = n
    return max_n


def max_ordered_vector(ordered_vector):
    return ordered_vector[0]


def max_heap(min_heap):
    return - heapq.heappop(min_heap)


def populate_heap(vector):
    vector = [-x for x in vector]
    heapq.heapify(vector)
    return vector
