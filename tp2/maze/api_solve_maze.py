import sys
from grafo import Grafo
from maze_printer import maze_to_string
from data_structs import StructList, StructArray


def get_and_validate_maze_size(str_maze):
    str_maze_as_lines = StructList(str_maze.splitlines())

    ui_n_columns = None
    i = 0
    for line in str_maze_as_lines:
        if i == 0:
            ui_n_columns = len(line)
        else:
            assert ui_n_columns == len(line)
        i = i + 1

    ui_n_rows = i

    assert ui_n_rows % 2 == 1
    assert ui_n_columns % 2 == 1

    return ui_n_rows, ui_n_columns


def validate_contour(str_maze, ui_n_rows, ui_n_columns):
    str_maze_as_lines = StructList(str_maze.splitlines())

    i = 0
    for line in str_maze_as_lines:
        if i % 2 == 0:
            assert line[0] == '+'
            assert line[ui_n_columns-1] == '+'
        else:
            assert line[0] == '|'
            assert line[ui_n_columns-1] == '|'

        if i == 0:
            j = 0
            for char in line:
                if j == 1:
                    assert char == ' '
                elif j % 2 == 0:
                    assert char == '+'
                else:
                    assert char == '-'
                j = j + 1

        if i == ui_n_rows-1:
            j = 0
            for char in line:
                if j == ui_n_columns-2:
                    assert char == ' '
                elif j % 2 == 0:
                    assert char == '+'
                else:
                    assert char == '-'
                j = j + 1

        i = i + 1


def obtain_adjacents_in_str_maze(str_maze_as_lines, ui_row, ui_column, ui_n_rows, ui_n_columns):
    adjacents = StructList([])

    row = int((ui_row - 1) / 2)
    column = int((ui_column - 1) / 2)

    if ui_row > 1 and str_maze_as_lines[ui_row-1][ui_column] == ' ':
        adjacents.append((row-1, column))
    if ui_row < ui_n_rows-2 and str_maze_as_lines[ui_row+1][ui_column] == ' ':
        adjacents.append((row+1, column))
    if ui_column > 1 and str_maze_as_lines[ui_row][ui_column-1] == ' ':
        adjacents.append((row, column-1))
    if ui_column < ui_n_columns-2 and str_maze_as_lines[ui_row][ui_column+2] == ' ':
        adjacents.append((row, column+1))

    return adjacents


def str_maze_to_maze(str_maze, ui_n_rows, ui_n_columns):
    str_maze_as_lines = StructArray(str_maze.splitlines())

    maze = Grafo()

    for i in range(len(str_maze_as_lines)):
        line = str_maze_as_lines[i]

        if i % 2 == 1:
            for j in range(len(line)):
                if j % 2 == 1:
                    row = int((i - 1) / 2)
                    column = int((j - 1) / 2)
                    maze.agregar_vertice((row, column))

                    adjacents = obtain_adjacents_in_str_maze(str_maze_as_lines, i, j, ui_n_rows, ui_n_columns)

                    for w in adjacents:
                        maze.agregar_arista((row, column), w, True)

    return maze


def find_path(maze, starting_node, finish_node):
    visited = set()
    fathers = {}
    stack = StructList([])

    visited.add(starting_node)
    fathers[starting_node] = None
    stack.append(starting_node)

    while len(stack) != 0:
        v = stack.pop()

        if v == finish_node:
            break

        for w in maze.obtener_adyacentes(v):
            if w not in visited:
                visited.add(w)
                fathers[w] = v
                stack.append(w)

    assert finish_node in visited, 'Could not reach the finish node, maze is invalid.'

    path = [finish_node]
    father = fathers[finish_node]
    while father is not None:
        path.append(father)
        father = fathers[father]

    return path


def print_str_maze_with_path(str_maze, path):
    str_maze_as_lines = StructArray(str_maze.splitlines())

    for row, column in path:
        s = str_maze_as_lines[ui_pos(row)]
        ui_line_replaced_with_path = s[:ui_pos(column)] + '*' + s[ui_pos(column) + 1:]
        str_maze_as_lines[ui_pos(row)] = ui_line_replaced_with_path

    for i in range(len(str_maze_as_lines)):
        line = str_maze_as_lines[i]
        print(line)


def ui_pos(pos):
    return (2 * pos) + 1


def solve_and_print_maze(str_maze):
    ui_n_rows, ui_n_columns = get_and_validate_maze_size(str_maze)
    validate_contour(str_maze, ui_n_rows, ui_n_columns)

    maze = str_maze_to_maze(str_maze, ui_n_rows, ui_n_columns)

    n_rows = int((ui_n_rows - 1) / 2)
    n_columns = int((ui_n_columns - 1) / 2)

    reconstructed_str_maze = maze_to_string(maze, n_rows, n_columns)
    path = find_path(maze, (0, 0), (n_rows-1, n_columns-1))

    print_str_maze_with_path(reconstructed_str_maze, path)
    print('Longitud: ' + str(len(path)))


def read_maze_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def main():
    assert len(sys.argv) == 2, 'Maze file not specified.'

    maze_file = sys.argv[1]
    str_maze = read_maze_from_file(maze_file)

    solve_and_print_maze(str_maze)


if __name__ == '__main__':
    main()
