from grafo import Grafo
from maze_printer import print_maze


def remove_nodes_for_exampe_4x4(maze):
    maze.agregar_arista((0, 0), (1, 0), True)
    maze.agregar_arista((1, 0), (1, 1), True)
    maze.agregar_arista((1, 1), (1, 2), True)
    maze.agregar_arista((1, 2), (1, 3), True)
    maze.agregar_arista((1, 3), (2, 3), True)
    maze.agregar_arista((2, 3), (3, 3), True)
    maze.agregar_arista((3, 3), (3, 4), True)
    maze.agregar_arista((3, 4), (4, 4), True)


def main():
    n_rows = 5
    n_columns = 5

    maze: Grafo = Grafo()

    for i in range(0, n_rows):
        for j in range(0, n_columns):
            node = (i, j)
            maze.agregar_vertice(node)
    print('Maze size: ' + str(maze.cant_vertices()))

    """
    for v in maze.obtener_vertices():
        row, column = v

        if row > 0:
            maze.agregar_arista(v, (row-1, column), True)
        if row < n_rows-1:
            maze.agregar_arista(v, (row+1, column), True)
        if column > 0:
            maze.agregar_arista(v, (row, column-1), True)
        if column < n_columns-1:
            maze.agregar_arista(v, (row, column+1), True)

    print(maze.obtener_adyacentes((0, 0)))
    print(maze.obtener_adyacentes((4, 4)))
    print(maze.obtener_adyacentes((2, 2)))
    """

    remove_nodes_for_exampe_4x4(maze)
    print_maze(maze, n_rows, n_columns)




if __name__ == '__main__':
    main()
