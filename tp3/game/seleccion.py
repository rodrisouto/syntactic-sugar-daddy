#!/usr/bin/env python3

import sys

import game_utils
import graph_utils


def city_with_more_spices(cities):

    max_spices =  max(map(lambda x: x.get_spices(), cities.values()))

    for city_name in cities:
        if cities[city_name].get_spices() == max_spices:
            return city_name


def chose_connected_cities(cities, distances):

    chosen = []

    for distance in distances:
        sorted_cities_by_spices = sorted(distances[distance], key=lambda x: cities[x].get_spices(), reverse=True)

        for city_name in sorted_cities_by_spices:
            chosen.append(city_name)

    return chosen


def chose_not_connected_cities(cities, already_chosen_as_set):

    not_chosen = list(filter(lambda x: x not in already_chosen_as_set, cities))

    return sorted(not_chosen, key=lambda x: cities[x].get_spices(), reverse=True)


# TODO do right
def player_1_selection(board, cities):

    choosen_metropolis = city_with_more_spices(cities)
    parents, distances = graph_utils.bfs(board, choosen_metropolis)

    chosen_connected = chose_connected_cities(cities, distances)
    chosen_not_connected = chose_not_connected_cities(cities, set(chosen_connected))

    return chosen_connected + chosen_not_connected


# Has the same logic as player 1.
def player_2_selection(board, cities):
    return player_2_selection(board, cities)


def print_cities(player_no, cities_names):

    filename = game_utils.get_selection_filename(player_no)

    text = '\n'.join(cities_names)
    with open(filename, "w+") as file:
        file.write(text)


def resolve_cities(player_no, board, cities):

    if player_no == 1:
        return player_1_selection(board, cities)
    elif player_no == 2:
        return player_2_selection(board, cities)


def main():

    player_no = int(sys.argv[1])
    cities_filename = sys.argv[2]
    routes_filename = sys.argv[3]

    board, cities = game_utils.load_empty_board(cities_filename, routes_filename)

    chosen = resolve_cities(player_no, board, cities)
    assert len(set(chosen)) == len(cities), '{} \n {}'.format(chosen, cities)
    print_cities(player_no, chosen)


if __name__ == '__main__':
    main()
