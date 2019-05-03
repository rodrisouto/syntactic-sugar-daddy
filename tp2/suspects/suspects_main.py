
import sys

from suspects import Person, find_suspects


def load_file(filename):
    people = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.split(',')
            entry = int(data[1])
            exit = int(data[2]) + entry
            people.append(Person(data[0], entry, exit))
    return people


def write_file(filename, suspects):
    with open(filename, 'w') as file:
        for group in suspects:
            file.write(str(group) + '\n')


if __name__ == "__main__":
    output = "sospechosos.txt"
    if len(sys.argv) == 3:
        output = sys.argv[2]
    elif len(sys.argv) != 2:
        print("Usage:\n\tpython3 suspects_main.py filename.txt")
    people = load_file(sys.argv[1])
    suspects = find_suspects(people)
    write_file(output, suspects)
