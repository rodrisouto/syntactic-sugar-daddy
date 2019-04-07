
import sys

from LinkedList import LinkedList
from max import *

def get_from_file(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        for line in file:
            numbers.append(int(line))
    return numbers


# load_other recieves a list and returns the structure needed by f_other
def cmp_f(numbers, f_vector, f_list, f_ord_vector, f_other, load_other):
    return [f_vector(numbers),
            f_list(LinkedList(numbers)),
            f_ord_vector(sorted(numbers, reverse=True)),
            f_other(load_other(numbers))]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:\n\tpython3 main.py numbers.txt function", sys.stderr)
        exit(1)
    numbers = get_from_file(sys.argv[1])
    func_name = sys.argv[2]

    results = []
    if func_name == "maximo":
        results = cmp_f(numbers, max_vector, max_list, max_ordered_vector, max_heap, load_heap)
    else:
        print("Function unknown: " + func_name, sys.stderr)
        exit(1)

    with open("resultado.txt", 'w') as file:
        file.writelines("\n".join([str(x) for x in results]))
    exit(0)
