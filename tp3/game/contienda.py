#!/usr/bin/env python3

import sys
from copy import copy, deepcopy

import game_utils

from empire import Empire


def discount_attacking_troops(cities, attack):

    for atk in attack:
        cities[atk[0]].discount_troops(atk[2])


def execute_attack(cities, cities_snapshot, attack):

    for atk in attack:
        attacking_city = cities_snapshot[atk[0]]
        assert attacking_city.get_owner() is not None, '{} {}'.format(atk, attacking_city)
        cities[atk[1]].receive_attack(attacking_city.get_owner(), atk[2])


def free_troopless_cities(cities):

    for city_name in cities:
        cities[city_name].free_if_troopless()


def resolve_contest(board, cities, empire_1, empire_2, attack_1, attack_2):

    discount_attacking_troops(cities, attack_1)
    discount_attacking_troops(cities, attack_2)

    # This is necessary because cities will change owners during attacks.
    cities_snapshot = dict(map(lambda x: deepcopy(x), cities.items()))

    execute_attack(cities, cities_snapshot, attack_1)
    execute_attack(cities, cities_snapshot, attack_2)

    free_troopless_cities(cities)






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
    game_utils.validate_attacks(board, empire_1, empire_2, attack_1, attack_2)

    resolve_contest(board, cities, empire_1, empire_2, attack_1, attack_2)
    # TODO print changed cities to files !!!!!

    print()
    print('cities: ' + str(cities))


if __name__ == "__main__":
    main()
