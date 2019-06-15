#!/usr/bin/env python3

import sys

import game_utils


def main():

    player_no = int(sys.argv[1])
    cities_filename = sys.argv[2]
    routes_filename = sys.argv[3]
    empire_1_filename = sys.argv[4]
    harvest_1_filename = sys.argv[5]
    empire_2_filename = sys.argv[6]
    harvest_2_filename = sys.argv[7]

    own_empire, rival_empire = game_utils.resolve_empires(player_no, empire_1_filename, empire_2_filename)
    print(own_empire)
    print(rival_empire)
    own_harvest, rival_harvest = game_utils.resolve_harvests(player_no, harvest_1_filename, harvest_2_filename)
    print(own_harvest)
    print(rival_harvest)

    board = game_utils.load_board(cities_filename, routes_filename)
    print(board)
    print(board.get_nodes())
    print(board.get_edges())

    game_utils.validate_empires(board, own_empire, rival_empire)

    # TODO apply logic !!!!!


if __name__ == "__main__":
    main()
