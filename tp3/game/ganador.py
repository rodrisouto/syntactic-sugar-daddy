#!/usr/bin/env python3

import sys

import game_utils
import graph_utils

from empire import Empire


def empire_has_requirements_to_win(board, own_harvest, rival_empire):

    if own_harvest > game_utils.get_harvest_limit_to_win():
        return True

    rival_metropolis = rival_empire.get_metropolis()
    parents, distances = graph_utils.bfs(board, rival_metropolis)

    if len(distances[1]) == 0:
        return True

    return False


def resolve_winner(round_no, board, empire_1, harvest_1, empire_2, harvest_2):

    if round_no > game_utils.get_rounds_limit():
        return untie(empire_1, harvest_1, empire_2, harvest_2)

    empire_1_can_win = empire_has_requirements_to_win(board, harvest_1, empire_2)
    empire_2_can_win = empire_has_requirements_to_win(board, harvest_2, empire_1)

    if empire_1_can_win and empire_2_can_win:
        return untie(empire_1, harvest_1, empire_2, harvest_2)
    elif empire_1_can_win:
        return empire_1.get_player()
    elif empire_2_can_win:
        return empire_2.get_player()
    else:
        return game_utils.get_no_winner()


def untie(empire_1, harvest_1, empire_2, harvest_2):

    # Untie by harvest.
    print('Untie by harvest.')
    print(harvest_1, harvest_2)
    if harvest_1 > harvest_2:
        return empire_1.get_player()
    elif harvest_2 > harvest_1:
        return empire_2.get_player()

    # Untie by amount of cities.
    print('Untie by amount of cities.')
    len_empire_1 = len(empire_1.get_original_troops_at_loading())
    len_empire_2 = len(empire_2.get_original_troops_at_loading())

    if len_empire_1 > len_empire_2:
        return empire_1.get_player()
    elif len_empire_2 > len_empire_1:
        return empire_2.get_player()

    # Untie by amount of troops.
    print('Untie by amount of troops.')
    troops_empire_1 = sum(empire_1.get_cities().values())
    troops_empire_2 = sum(empire_2.get_cities().values())

    if troops_empire_1 > troops_empire_2:
        return empire_1.get_player()
    elif troops_empire_2 > troops_empire_1:
        return empire_2.get_player()

    return game_utils.get_no_winner()


def print_winner(winner):

    with open(game_utils.get_winner_file(), 'w') as file:
        file.write(str(winner))


def main():

    round_no = int(sys.argv[1])
    cities_filename = sys.argv[2]
    routes_filename = sys.argv[3]
    empire_1_filename = sys.argv[4]
    harvest_1_filename = sys.argv[5]
    empire_2_filename = sys.argv[6]
    harvest_2_filename = sys.argv[7]

    empire_1, empire_2 = game_utils.resolve_empires(1, empire_1_filename, empire_2_filename)
    print(empire_1)
    print(empire_2)
    harvest_1, harvest_2 = game_utils.resolve_harvests(1, harvest_1_filename, harvest_2_filename)
    print(harvest_1)
    print(harvest_2)

    board, cities = game_utils.load_empty_board(cities_filename, routes_filename)
    print(board)
    print(board.get_nodes())
    print(board.get_edges())
    print()
    print('cities: ' + str(cities))
    game_utils.assign_cities(cities, empire_1, empire_2)
    print()
    print('cities: ' + str(cities))

    game_utils.validate_empires(board, empire_1, empire_2)

    # TODO apply logic !!!!!
    winner = resolve_winner(round_no, board, empire_1, harvest_1, empire_2, harvest_2)
    print('!!!! winner: ' + str(winner))
    print_winner(winner)


if __name__ == "__main__":
    main()
