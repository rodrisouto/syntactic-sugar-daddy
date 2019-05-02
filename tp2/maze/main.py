import sys
from maze_generator import generate_maze_with_dfs
from maze_printer import print_maze


MAZE_GENERATORS = {
    'd&c': None,
    'dfs': generate_maze_with_dfs
}


def main():
    assert len(sys.argv) == 4, 'Three parameters are required.'

    n_rows = int(sys.argv[2])
    n_columns = int(sys.argv[3])
    assert n_rows > 0, 'There must be at least 1 row.'
    assert n_columns > 0, 'There must be at least 1 column.'

    maze_generator_method = sys.argv[1]
    assert maze_generator_method in MAZE_GENERATORS, \
        'Valid maze_generators methods are: ' + ', '.join([str(x) for x in MAZE_GENERATORS.keys()]) + '.'

    print('Maze generated with ' + maze_generator_method + ':')
    maze = MAZE_GENERATORS[maze_generator_method](n_rows, n_columns)
    print_maze(maze, n_rows, n_columns)


if __name__ == '__main__':
    main()
