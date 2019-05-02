from grafo import Grafo


def ui_pos(maze_pos):
    return (2 * maze_pos) + 1


def initialize_ui_maze_with_no_edges(ui_maze, ui_n_rows, ui_n_columns):
    for i in range(0, ui_n_rows):
        ui_row = []
        ui_maze.append(ui_row)
        for j in range(0, ui_n_columns):
            ui_row.append('+')

    for i in range(0, ui_n_rows):
        for j in range(0, ui_n_columns):
            if i % 2 == 0 and j % 2 == 1:
                ui_maze[i][j] = '-'
            if j % 2 == 0 and i % 2 == 1:
                ui_maze[i][j] = '|'

    ui_maze[0][1] = ' '
    ui_maze[ui_n_rows-1][ui_n_columns-2] = ' '


def add_adjacents_to_ui_maze(ui_maze, maze: Grafo, n_rows, n_columns):
    for i in range(0, n_rows):
        for j in range(0, n_columns):
            ui_maze[ui_pos(i)][ui_pos(j)] = ' '

            adjacents = maze.obtener_adyacentes((i, j))

            for r, c in adjacents:
                ui_maze[ui_pos(i) + (r-i)][ui_pos(j) + (c-j)] = ' '


def ui_row_to_string(ui_row):
    return ''.join([str(x) for x in ui_row])


def ui_maze_to_string(ui_maze):
    return '\n'.join(ui_row_to_string(ui_row) for ui_row in ui_maze)


def maze_to_string(maze: Grafo, n_rows, n_columns):

    ui_n_rows = (2 * n_rows) + 1
    ui_n_columns = (2 * n_columns) + 1

    ui_maze = []

    initialize_ui_maze_with_no_edges(ui_maze, ui_n_rows, ui_n_columns)
    add_adjacents_to_ui_maze(ui_maze, maze, n_rows, n_columns)

    return ui_maze_to_string(ui_maze)

        
def maze_main():
    return

    
if __name__ == '__main__':
    maze_main()
