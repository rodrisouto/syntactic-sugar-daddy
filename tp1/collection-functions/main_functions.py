
import sys

from functools import partial

sys.path.append('../utils/')

from MeanCalculator import populate_mean_calculator
from StdDeviationCalculator import populate_std_calculator
from SortedList import populate_sorted_list
from median import median_vector, median_list, median_ordered_vector, median_sorted_list
from mean import *
from max import *
from mode import mode_vector, mode_sorted_list, mode_ordered_vector, mode_list
from permutations import permutations_vector, permutations_list, permutations_ordered_vector, permutations_sorted_list
from standard_deviation import standard_deviation_STD_calculator, standard_deviation_ordered_vector, \
    standard_deviation_list, standard_deviation_vector
from variations import variations_vector, variations_list, variations_ordered_vector, variations_sorted_list
from variations_with_repetitions import variations_with_repetitions_vector, \
    variations_with_repetitions_ordered_vector, variations_with_repetitions_list, \
    variations_with_repetitions_sorted_list


def get_from_file(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        for line in file:
            numbers.append(int(line))
    return numbers


def __populate_to_do(list):
    return list


def __to_do(list):
    return "TODO"


# populate_other recieves a list and returns the structure needed by f_other
def run_all(numbers, f_vector, f_list, f_ord_vector, f_other, populate_other):
    return [f_vector(numbers[:]),
            f_list(numbers[:]),
            f_ord_vector(sorted(numbers, reverse=True)),
            f_other(populate_other(numbers[:]))]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:\n\tpython3 main_functions.py numbers.txt function", file=sys.stderr)
        exit(1)

    numbers = get_from_file(sys.argv[1])
    func_name = sys.argv[2]

    groups = 1
    if func_name in ["variaciones", "variaciones_repeticion"]:
        groups = int(input("Ingrese el tamaño de los grupos (menor o igual a {}): ".format(len(numbers))))

    func_args = {
        "maximo": (max_vector, max_list, max_ordered_vector, max_heap, populate_heap),
        "media":  (mean_vector, mean_list, mean_ordered_vector, mean_calculator, populate_mean_calculator),
        "mediana": (median_vector, median_list, median_ordered_vector, median_sorted_list, populate_sorted_list),
        "moda": (mode_vector, mode_list, mode_ordered_vector, mode_sorted_list, populate_sorted_list),
        "permutaciones": (permutations_vector, permutations_list, permutations_ordered_vector, permutations_sorted_list, populate_sorted_list),
        "desviacion_estandar": (standard_deviation_vector, standard_deviation_list, standard_deviation_ordered_vector,
                                standard_deviation_STD_calculator, populate_std_calculator),
        "variaciones_repeticion": (partial(variations_with_repetitions_vector, r=groups),
                                   partial(variations_with_repetitions_list, r=groups),
                                   partial(variations_with_repetitions_ordered_vector, r=groups),
                                   partial(variations_with_repetitions_sorted_list, r=groups), populate_sorted_list),
        "variaciones": (partial(variations_vector, r=groups), partial(variations_list, r=groups),
                        partial(variations_ordered_vector, r=groups), partial(variations_sorted_list, r=groups), populate_sorted_list)
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
