#!/usr/bin/env python3

from typing import Dict, Tuple

from load_board import load_board as do_load_board

from city import City
from empire import Empire


def get_harvest_limit_to_win():
    return 100


def get_rounds_limit():
    return 50


def get_no_winner():
    return ''


def get_winner_file():
    return 'ganador.txt'


def get_empire_filename(player_no):
    return 'imperio{}.txt'.format(player_no)


def get_empire_temp_filename(player_no):
    return 'imperio{}_temp.txt'.format(player_no)


def get_harvest_filename(player_no):
    return 'cosecha{}.txt'.format(player_no)


def get_harvest_temp_filename(player_no):
    return 'cosecha{}_temp.txt'.format(player_no)


def get_selection_filename(player_no):
    return 'seleccion{}.txt'.format(player_no)


def get_attack_filename(player_no):
    return 'ataque{}.txt'.format(player_no)


def _validate_empire(board, own_empire, rival_empire):

    for city_name in own_empire.get_original_troops_at_loading():
        assert city_name in board, 'City {} was not in the board: {}.'.format(city_name, board.get_nodes())
        assert city_name not in rival_empire.get_original_troops_at_loading(), 'City {} was in the rival empire: {}.'.format(city_name, rival_empire)
        assert own_empire.get_original_troops_at_loading()[city_name] >= 0, 'City {} has less than 0 troops'.format(city_name)


def validate_empires(board, empire1, empire2):

    _validate_empire(board, empire1, empire2)
    _validate_empire(board, empire2, empire1)


def load_empty_board(cities_filename, routes_filename):
    return do_load_board(cities_filename, routes_filename)


def resolve_empire(player_no, empire_filename) -> Empire:

    cities_counter = 0
    metropolis = None
    empire_troops = {}

    file = open(empire_filename)

    for city in file.read().split('\n'):
        if city == '':
            continue

        try:
            city_name, troops = city.split(',')
        except Exception:
            raise ValueError('not enough values to unpack. {}'.format(city))

        assert city_name not in empire_troops, 'City {} was already in the empire.'.format(city_name)

        if cities_counter == 0:
            metropolis = city_name

        empire_troops[city_name] = int(troops)
        cities_counter += 1

    empire = Empire(player_no, metropolis, empire_troops)

    return empire


def resolve_empires(player_no: int, empire_1_filename: str, empire_2_filename: str) -> Tuple[Empire, Empire]:

    empire_1: Empire = resolve_empire(1, empire_1_filename)
    empire_2: Empire = resolve_empire(2, empire_2_filename)

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


def resolve_attack(attack_filename):

    attack = []

    with open(attack_filename, 'r') as file:
        for line in file:
            if line == '':
                continue

            attack_tuple = line.split(',')
            assert len(attack_tuple) == 3, 'Error {}'.format(attack_tuple)
            src_city = attack_tuple[0]
            dst_city = attack_tuple[1]
            troops = int(attack_tuple[2])
            assert troops > 0, 'Troops can not be negative {}'.format(attack_tuple)

            attack.append((src_city, dst_city, troops))

    return attack


def resolve_attacks(attack_1_filename, attack_2_filename):
    return resolve_attack(attack_1_filename), resolve_attack(attack_2_filename)


def validate_attack(board, own_empire, rival_empire, attack):

    own_placed_troops = own_empire.get_original_troops_at_loading()

    for atk in attack:
        assert len(atk) == 3, 'Error in atk len {}'.format(atk)
        assert atk[0] in own_placed_troops, 'Source City was not in own empire {}, {}'.format(atk, own_empire)
        assert atk[1] not in own_placed_troops, 'Destination City was in own empire {}, {}'.format(atk, rival_empire)
        assert int(atk[2]) > 0, 'Troops can not be negative {}'.format(atk)

        assert own_placed_troops[atk[0]] >= int(atk[2])
        assert board.are_adjacents(atk[0], atk[1]), 'Cities are not adjacent: {}'.format(atk)


def validate_attacks(board, empire_1, empire_2, attack_1, attack_2):

    validate_attack(board, empire_1, empire_2, attack_1)
    validate_attack(board, empire_2, empire_1, attack_2)


def _assign_cities_of_empire(cities: Dict[str, City], owner, empire_troops):

    for city_name in empire_troops:
        cities[city_name].assign_owner(owner, empire_troops[city_name])


def assign_cities(cities: Dict[str, City], own_empire, rival_empire):

    _assign_cities_of_empire(cities, own_empire.get_player(), own_empire.get_original_troops_at_loading())
    _assign_cities_of_empire(cities, rival_empire.get_player(), rival_empire.get_original_troops_at_loading())


def find_metropolis(cities_filename):

    metropolis_1 = None
    metropolis_2 = None

    with open(cities_filename, "r") as file:
        i = 0
        for line in file:
            city_tuple = line.split(',')
            assert len(city_tuple) == 2

            if i == 0:
                metropolis_1 = city_tuple[0]
            if i == 1:
                metropolis_2 = city_tuple[0]

            i += 1

    return metropolis_1, metropolis_2
