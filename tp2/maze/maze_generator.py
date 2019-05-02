import random
from grafo import Grafo
from maze_printer import print_maze


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
    return neighbors


def maze_generator_dfs(maze, n_rows, n_columns):
    visited = set()

    starting_node = (0, 0)
    visited.add(starting_node)
    frontier = [starting_node]

    while len(frontier) != 0:
        v = frontier.pop(random.randrange(len(frontier)))
        row, column = v

        neighbors = obtain_neighbors(row, column, n_rows, n_columns)

        for w in neighbors:
            if w not in visited:
                visited.add(w)
                frontier.append(w)
                maze.agregar_arista(v, w, True)


def main():
    n_rows = 5
    n_columns = 5

    maze: Grafo = Grafo()

    for i in range(0, n_rows):
        for j in range(0, n_columns):
            node = (i, j)
            maze.agregar_vertice(node)

    # remove_nodes_for_exampe_4x4(maze)
    print('Maze generated with DFS:')
    maze_generator_dfs(maze, n_rows, n_columns)
    print_maze(maze, n_rows, n_columns)


if __name__ == '__main__':
    main()
