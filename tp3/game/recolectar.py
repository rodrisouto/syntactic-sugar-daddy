#!/usr/bin/env python3

import sys

import game_utils


# TODO do Fluxily
def obtain_new_harvest(board):
    return 10


def print_harvest(harvest_filename, final_harvest):

    file = open(harvest_filename, "w+")

    file.write(final_harvest + '\n')
    file.close()


def obtain_previous_harvest(harvest_filename):

    file = open(harvest_filename, 'r')
    previous_harvest = int(file.read())
    print(previous_harvest)
    file.close()

    return previous_harvest


def resolve_harvest(harvest_filename, board):

    previous_harvest = obtain_previous_harvest(harvest_filename)
    new_harvest = obtain_new_harvest(board)
    final_harvest = previous_harvest
    print_harvest(harvest_filename, final_harvest)


def obtain_owned_cities(owned_cities_filename):

    file = open(owned_cities_filename)

    owned_cities = []
    for city_name in file.read().split('\n'):
        owned_cities.append(city_name)
    print('!!!! owned_cities', owned_cities)

    return owned_cities


def main():

    player_no = int(sys.argv[1])
    cities_filename = sys.argv[2]
    routes_filename = sys.argv[3]
    owned_cities_filename = sys.argv[4]

    owned_cities = obtain_owned_cities(owned_cities_filename)
    board = game_utils.load_board(cities_filename, routes_filename)

    # cities_names = resolve_cities(player_no, board)
    filename = 'cosecha{}.txt\n'.format(player_no)

    resolve_harvest(filename, owned_cities)


if __name__ == '__main__':
    main()
