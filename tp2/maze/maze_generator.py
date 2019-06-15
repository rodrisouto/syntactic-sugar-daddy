import random
import math
from grafo import Grafo
from maze_printer import maze_to_string
from data_structs import StructList


def add_nodes_to_maze(maze, n_rows, n_columns):
    for i in range(n_rows):
        for j in range(n_columns):
            node = (i, j)
            maze.add_node(node)


def obtain_neighbors(row, column, n_rows, n_columns):
    neighbors = []

    if row > 0:
        neighbors.append((row - 1, column))
    if row < n_rows - 1:
        neighbors.append((row + 1, column))
    if column > 0:
        neighbors.append((row, column - 1))
    if column < n_columns - 1:
        neighbors.append((row, column + 1))

    random.shuffle(neighbors)
    return StructList(neighbors)


def do_generate_maze_with_dfs(maze, n_rows, n_columns):
    visited = set()
    frontier = StructList([])

    starting_node = (0, 0)
    visited.add(starting_node)
    frontier.append(starting_node)

    while len(frontier) != 0:
        v = frontier.pop(random.randrange(len(frontier)))
        row, column = v

        neighbors = obtain_neighbors(row, column, n_rows, n_columns)

        for w in neighbors:
            if w not in visited:
                visited.add(w)
                frontier.append(w)
                maze.add_edge(v, w, True)


def generate_maze_with_dfs(n_rows, n_columns):
    maze = initialize_maze(n_rows, n_columns)
    do_generate_maze_with_dfs(maze, n_rows, n_columns)

    return maze


def split_vertically(maze, start_row, end_row, start_column, end_column):
    middle = (start_row + end_row) // 2

    _generate_maze_with_dyc(maze, start_row, middle, start_column, end_column)
    _generate_maze_with_dyc(maze, middle + 1, end_row, start_column, end_column)

    merging_column = random.randrange(start_column, end_column + 1)
    maze.add_edge((middle, merging_column), (middle + 1, merging_column), True)


def split_horizontally(maze, start_row, end_row, start_column, end_column):
    middle = (start_column + end_column) // 2

    _generate_maze_with_dyc(maze, start_row, end_row, start_column, middle)
    _generate_maze_with_dyc(maze, start_row, end_row, middle + 1, end_column)

    merging_row = random.randrange(start_row, end_row + 1)
    maze.add_edge((merging_row, middle), (merging_row, middle + 1), True)


def choose_how_to_split_randomly(maze, start_row, end_row, start_column, end_column):
    rand = random.randrange(2)
    assert rand != 2

    if rand == 0:
        split_vertically(maze, start_row, end_row, start_column, end_column)
    else:
        split_horizontally(maze, start_row, end_row, start_column, end_column)


def _generate_maze_with_dyc(maze, start_row, end_row, start_column, end_column):
    if end_row == start_row and end_column == start_column:
        return

    rows = 1 + end_row - start_row
    columns = 1 + end_column - start_column

    if rows > columns:
        split_vertically(maze, start_row, end_row, start_column, end_column)
    elif columns > rows:
        split_horizontally(maze, start_row, end_row, start_column, end_column)
    else:
        choose_how_to_split_randomly(maze, start_row, end_row, start_column, end_column)

    return


def generate_maze_with_dyc(n_rows, n_columns):
    maze = initialize_maze(n_rows, n_columns)
    _generate_maze_with_dyc(maze, 0, n_rows-1, 0, n_columns-1)

    return maze


def initialize_maze(n_rows, n_columns):
    maze: Grafo = Grafo()
    add_nodes_to_maze(maze, n_rows, n_columns)

    return maze


# This is only for debugging.
def main():
    maze = generate_maze_with_dyc(10, 20)
    print(maze_to_string(maze, 10, 20))


if __name__ == '__main__':
    main()
