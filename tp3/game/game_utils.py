#!/usr/bin/env python3

from load_board import load_board as do_load_board


def get_empire_filename(player_no):
    return 'imperio{}.txt'.format(player_no)


def get_empire_temp_filename(player_no):
    return 'imperio{}_temp.txt'.format(player_no)


def get_harvest_filename(player_no):
    return 'harvest{}.txt'.format(player_no)


def get_harvest_temp_filename(player_no):
    return 'harvest{}_temp.txt'.format(player_no)


def get_selection_filename(player_no):
    return 'seleccion{}.txt'.format(player_no)


def _validate_empire(board, own_empire, rival_empire):

    for city in own_empire:
        assert city in board.get_nodes(), 'City {} was not in the board: {}.'.format(city, board.get_nodes())
        assert city not in rival_empire, 'City {} was in the rival empire: {}.'.format(city, rival_empire)


def validate_empires(board, empire1, empire2):

    _validate_empire(board, empire1, empire2)
    _validate_empire(board, empire2, empire1)


def load_board(cities_filename, routes_filename):
    return do_load_board(cities_filename, routes_filename)


def resolve_empire(empire_filename):

    empire = {}

    file = open(empire_filename)

    for city in file.read().split('\n'):
        if city == '':
            continue

        try:
            city_name, troops = city.split(',')
        except Exception:
            print('\n\n{}\n\n'.format(city))
            raise ValueError('not enough values to unpack.')

        if city_name in empire:
            raise Exception('City {} was already in the empire.'.format(city_name))

        empire[city_name] = int(troops)

    return empire


def resolve_empires(player_no, empire_1_filename, empire_2_filename):

    empire_1: dict = resolve_empire(empire_1_filename)
    empire_2: dict = resolve_empire(empire_2_filename)

    if player_no == 1:
        return empire_1, empire_2
    else:
        return empire_2, empire_1


def resolve_harvest(harvest_filename):

    with open(harvest_filename, 'r') as file:
        for line in file:
            harvest_str = line.split('\n')[0]
            return int(harvest_str)


def resolve_harvests(player_no, harvest_1_filename, harvest_2_filename):

    harvest_1: int = resolve_harvest(harvest_1_filename)
    harvest_2: int = resolve_harvest(harvest_2_filename)

    if player_no == 1:
        return harvest_1, harvest_2
    else:
        return harvest_2, harvest_1
