#!/usr/bin/env python3

import sys
from typing import List

import game_utils


def validate_selection(selection, all_cities):

    assert len(selection) == len(all_cities)
    for city in selection:
        assert city in all_cities, '{} | {} vs {}'.format(city, selection, all_cities)


def load_selection(filename, all_cities):

    selection = []

    with open(filename, 'r') as file:
        cities_txt = file.read()
        for city_name in cities_txt.split('\n'):
            if city_name != '':
                selection.append(city_name)

    validate_selection(selection, all_cities)
    print(selection)
    return selection


def resolve_all_cities(filename):

    all_cities = set()

    with open(filename, 'r') as file:
        cities_txt = file.read()
        for city_name in cities_txt.split('\n'):
            if city_name != '':
                all_cities.add(city_name.split(',')[0])

    return all_cities


def resolve_empires(selection_1, selection_2):

    i, j = 0, 0
    empire_1, empire_2 = list(), list()
    assigned_cities = set()
    player_1_chooses = True

    while len(assigned_cities) < len(selection_1):

        if player_1_chooses:
            if len(empire_1) >= len(selection_1):
                player_1_chooses = False
            elif selection_1[i] not in empire_2:
                city = selection_1[i]
                empire_1.append(city)
                assigned_cities.add(city)
                player_1_chooses = False
            i += 1

        else:
            if len(empire_2) >= len(selection_2):
                player_1_chooses = True
            elif selection_2[j] not in empire_1:
                city = selection_2[j]
                empire_2.append(city)
                assigned_cities.add(city)
                player_1_chooses = True
            j += 1

    # validation !!!!
    for city in empire_1:
        assert city not in empire_2, 'city: {}'.format(city)

    return empire_1, empire_2


def print_empire(empire, empire_no):

    with open(game_utils.get_empire_filename(empire_no), 'w') as file:
        for city in empire:
            file.write('{},1\n'.format(city))


def main():

    cities_filename = sys.argv[1]
    routes_filename = sys.argv[2]
    selection_1_filename = sys.argv[3]
    selection_2_filename = sys.argv[4]

    all_cities = resolve_all_cities(cities_filename)
    selection_1: List[str] = load_selection(selection_1_filename, all_cities)
    selection_2: List[str] = load_selection(selection_2_filename, all_cities)

    empire_1, empire_2 = resolve_empires(selection_1, selection_2)

    print_empire(empire_1, 1)
    print_empire(empire_2, 2)


if __name__ == '__main__':
    main()
