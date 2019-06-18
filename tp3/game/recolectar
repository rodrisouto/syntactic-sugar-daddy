#!/usr/bin/env python3

import sys

import game_utils
import graph_utils

from graph import DirectedGraph


# TODO do Fluxily
def obtain_new_harvest(board, empire):

    own_cities = set(empire.get_original_troops_at_loading().keys())
    board_with_own_cities = graph_utils.generate_directed_subgraph(board, own_cities)

    ford


def print_harvest(harvest_filename, final_harvest):

    with open(harvest_filename, "w+") as file:
        file.write(str(final_harvest))


def obtain_previous_harvest(harvest_filename):

    with open(harvest_filename, 'w+') as file:
        text = file.read()
        if text == '':
            previous_harvest = 0
        else:
            previous_harvest = int(text)

    return previous_harvest


def resolve_harvest(harvest_filename, board, cities, empire):

    previous_harvest = obtain_previous_harvest(harvest_filename)

    new_harvest = obtain_new_harvest(board, empire)
    final_harvest = previous_harvest + new_harvest

    print_harvest(harvest_filename, final_harvest)


def main():

    player_no = int(sys.argv[1])
    cities_filename = sys.argv[2]
    routes_filename = sys.argv[3]
    empire_filename = sys.argv[4]

    empire = game_utils.resolve_empire(player_no, empire_filename)
    board, cities = game_utils.load_empty_board(cities_filename, routes_filename)

    harvest_filename = game_utils.get_harvest_filename(player_no)

    resolve_harvest(harvest_filename, board, cities, empire)


if __name__ == '__main__':
    main()
