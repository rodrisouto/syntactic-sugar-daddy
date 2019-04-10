
import sys

from utils.LinkedList import LinkedList
from mean import *
from max import *


def get_from_file(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        for line in file:
            numbers.append(int(line))
    return numbers


# populate_other recieves a list and returns the structure needed by f_other
def run_all(numbers, f_vector, f_list, f_ord_vector, f_other, populate_other):
    return [f_vector(numbers),
            f_list(LinkedList(numbers)),
            f_ord_vector(sorted(numbers, reverse=True)),
            f_other(populate_other(numbers))]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:\n\tpython3 main.py numbers.txt function", file=sys.stderr)
        exit(1)

    numbers = get_from_file(sys.argv[1])
    func_name = sys.argv[2]

    func_args = {
        "maximo": (max_vector, max_list, max_ordered_vector, max_heap, populate_heap),
        "media":  (mean_vector, mean_list, mean_ordered_vector, mean_calculator, populate_mean_calculator)
    }

    try:
        args = func_args[func_name]
    except KeyError:
        print("Function unknown: " + func_name, file=sys.stderr)
        exit(1)

    results = run_all(numbers, *func_args[func_name])
    with open("resultado.txt", 'w') as file:
        file.write("\n".join([str(x) for x in results]))
    exit(0)



