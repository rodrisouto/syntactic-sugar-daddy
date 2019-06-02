#!/usr/bin/env python3

import sys

from load_board import load_board


# TODO do right
def player_1_selection(board):

    cities_names = list(board.get_nodes())
    cities_names = sorted(cities_names, key=lambda x: len(x))

    return cities_names


# TODO do right
def player_2_selection(board):

    cities_names = list(board.get_nodes())
    cities_names = sorted(cities_names, key=lambda x: len(x), reverse=True)

    return cities_names


def print_cities(filename, cities_names):

    file = open(filename, "w+")

    for city_name in cities_names:
        file.write(city_name + '\n')

    file.close()


def resolve_cities(player_no, board):

    if player_no == 1:
        return player_1_selection(board)
    elif player_no == 2:
        return player_2_selection(board)


def main():

    player_no = int(sys.argv[1])
    cities_filename = sys.argv[2]
    routes_filename = sys.argv[3]

    board = load_board(cities_filename, routes_filename)

    cities_names = resolve_cities(player_no, board)
    filename = 'seleccion{}.txt'.format(player_no)

    print_cities(filename, cities_names)


if __name__ == '__main__':
    main()
