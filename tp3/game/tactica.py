#!/usr/bin/env python3

import sys

import game_utils
import graph_utils

from empire import Empire


def resolve_attacks(board, cities, own_empire):

    metropolis = own_empire.get_metropolis()

    parents, distances = graph_utils.bfs(board, metropolis)

    print()
    print(parents)
    print(distances)

    return decide_attacks(board, cities, own_empire, distances)


def decide_attacks(board, cities, own_empire, distances):

    attack = []
    amount_of_owned_cities = len(own_empire.get_placed_troops())

    for distance in distances:
        cities_at_distance = distances[distance]

        for city_name in cities_at_distance:
            if int(amount_of_owned_cities * 0.33) < len(attack):
                break

            city = cities[city_name]
            if city.get_owner() != own_empire.get_player():
                atk_opt = decide_if_attack_city(board, cities, city, own_empire.get_player())

                if atk_opt is not None:
                    assert len(atk_opt) == 3
                    attack.append(atk_opt)

    return attack


def decide_if_attack_city(board, cities, rival_city, player_no):

    _, rival_city_distances = graph_utils.bfs(board, rival_city.get_name())

    for city_name in rival_city_distances[1]:
        adjacent_city = cities[city_name]

        if adjacent_city.get_owner() == player_no and adjacent_city.get_troops() > rival_city.get_troops() + 2:
            return adjacent_city.get_name(), rival_city.get_name(), str(rival_city.get_troops() + 1)

    return None


def print_attack(player_no, attack):

    # !!!!
    print(attack)
    text = '\n'.join(map(lambda atk: ','.join(atk), attack))
    print('print_attack: {}'.format(text))
    with open(game_utils.get_attack_filename(player_no), 'w') as file:
        file.write(text)


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

    board, cities = game_utils.load_empty_board(cities_filename, routes_filename)
    print(board)
    print(board.get_nodes())
    print(board.get_edges())

    print('cities: ' + str(cities))
    game_utils.assign_cities(cities, own_empire, rival_empire)
    print()
    print('cities: ' + str(cities))

    game_utils.validate_empires(board, own_empire, rival_empire)

    # TODO apply logic !!!!!
    attack = resolve_attacks(board, cities, own_empire)
    print_attack(player_no, attack)


if __name__ == "__main__":
    main()
