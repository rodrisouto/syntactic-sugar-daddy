
import sys

from MeanCalculator import populate_mean_calculator
from StdDeviationCalculator import populate_std_calculator
from SortedList import populate_sorted_list
from median import median_vector, median_list, median_ordered_vector, median_sorted_list
from mean import *
from max import *
from mode import mode_vector, mode_sorted_list, mode_ordered_vector, mode_list
from permutations import permutations_vector, permutations_list, permutations_ordered_vector
from standard_deviation import standard_deviation_STD_calculator, standard_deviation_ordered_vector, \
    standard_deviation_list, standard_deviation_vector


def get_from_file(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        for line in file:
            numbers.append(int(line))
    return numbers


# populate_other recieves a list and returns the structure needed by f_other
def run_all(numbers, f_vector, f_list, f_ord_vector, f_other, populate_other):
    return [f_vector(numbers),
            f_list(numbers),
            f_ord_vector(sorted(numbers, reverse=True)),
            f_other(populate_other(numbers))]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:\n\tpython3 main_functions.py numbers.txt function", file=sys.stderr)
        exit(1)

    numbers = get_from_file(sys.argv[1])
    func_name = sys.argv[2]

    func_args = {
        "maximo": (max_vector, max_list, max_ordered_vector, max_heap, populate_heap),
        "media":  (mean_vector, mean_list, mean_ordered_vector, mean_calculator, populate_mean_calculator),
        "mediana": (median_vector, median_list, median_ordered_vector, median_sorted_list, populate_sorted_list),
        "moda": (mode_vector, mode_list, mode_ordered_vector, mode_sorted_list, populate_sorted_list),
        "permutaciones": (permutations_vector, permutations_list, permutations_ordered_vector, mode_sorted_list, populate_sorted_list), # TODO: our structure
        "std": (standard_deviation_vector, standard_deviation_list, standard_deviation_ordered_vector, standard_deviation_STD_calculator, populate_std_calculator)
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



