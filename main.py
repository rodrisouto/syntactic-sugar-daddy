import sys
import csv
from itertools import groupby
from typing import List, Any

sys.path.append('/home/rodrigosouto/projects/facultad/tda/syntactic-sugar-daddy/utils/')
sys.path.append('/home/rodrigosouto/projects/facultad/tda/syntactic-sugar-daddy/gale-shapley/')
from people import Person
from gale_shapley_super import gale_shapley_super_stable


def obtain_raw_players(players_path):
    raw_players = []

    with open(players_path, 'r') as players_file:
        reader = csv.reader(players_file)
        for row in reader:
            raw_players.append(row)

    return raw_players


def obtain_players(raw_players):
    players = []
    players_dict = {}

    for raw_player in raw_players:
        player_name = raw_player[1]
        new_player = Person(player_name)

        players_dict[player_name] = new_player
        players.append(new_player)

    for raw_player in raw_players:
        set_preferences_for_player(raw_player, players_dict)

    return players


def set_preferences_for_player(raw_player, players_dict):

    player_name = raw_player[1]

    grouped_preferences = get_grouped_preferences_of_raw_player_by_score(raw_player)

    tied_preferences: List[List[Any]] = []

    for score, person in grouped_preferences:
        names_per_score = list(map(lambda x: x[0], person))
        players_per_score = list(map(lambda x: players_dict[x], names_per_score))

        tied_preferences.append(players_per_score)

    player = players_dict[player_name]
    player.set_preferences(tied_preferences)


def get_grouped_preferences_of_raw_player_by_score(raw_player):

    preferences_path = raw_player[2]
    preferences = []

    with open(preferences_path, 'r') as preferences_file:
        reader = csv.reader(preferences_file)
        for row in reader:
            preferences.append(row)

    sorted_preferences = sorted(preferences, key=lambda x: x[1], reverse=True)

    return groupby(sorted_preferences, lambda x: x[1])


if __name__ == '__main__':

    assert len(sys.argv) == 3, 'Two parameters are required.'

    number_of_players = int(sys.argv[1])
    assert number_of_players % 2 == 0, 'There must be a pair amount of players.'

    players_path = sys.argv[2]

    raw_players = obtain_raw_players(players_path)

    assert number_of_players == len(raw_players), \
        'In the players file there must be the same number of players as passed in parameters.'

    players = obtain_players(raw_players)

    print('API Validation')
    print('Players: ' + str(players))
    print()
    for p in players:
        print(p.get_preferred())
    print()

    half = int(len(players) / 2)

    best_half = players[:half]
    worst_half = players[half:]

    print(best_half)
    print(worst_half)

    pairs = gale_shapley_super_stable(best_half, worst_half)

    print()
    print('The matches for the tournament are:')
    for pair in pairs:
        final_pair = tuple(map(lambda x: x.name, pair))
        print('\t' + str(final_pair))
