#!/usr/bin/env python3

import sys

import game_utils


def main():

    cities_filename = sys.argv[1]
    routes_filename = sys.argv[2]
    empire_1_filename = sys.argv[3]
    empire_2_filename = sys.argv[4]
    attack_1_filename = sys.argv[5]
    attack_2_filename = sys.argv[6]

    empire_1, empire_2 = game_utils.resolve_empires(1, empire_1_filename, empire_2_filename)
    print(empire_1)
    print(empire_2)
    attack_1, attack_2 = game_utils.resolve_attacks(attack_1_filename, attack_2_filename)
    print(attack_1)
    print(attack_2)

    board = game_utils.load_board(cities_filename, routes_filename)
    print(board)
    print(board.get_nodes())
    print(board.get_edges())

    game_utils.validate_empires(board, empire_1, empire_2)
    game_utils.validate_attacks(empire_1, empire_2, attack_1, attack_2)

    # TODO apply logic !!!!!


if __name__ == "__main__":
    main()
