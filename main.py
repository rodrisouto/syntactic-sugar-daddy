import sys
import csv
from random import shuffle
from itertools import groupby
from typing import List, Any

sys.path.append('/home/rodrigosouto/projects/facultad/tda/syntactic-sugar-daddy/utils/')
sys.path.append('/home/rodrigosouto/projects/facultad/tda/syntactic-sugar-daddy/gale-shapley/')
from people import Person
from people_simple import Person as SimplePerson
from gale_shapley_super import gale_shapley_super_stable
from gale_shapley import gale_shapley


flatten = lambda l: [item for sublist in l for item in sublist]

lambda_solve_tie_alphabetically = lambda list: solve_tie_alphabetically(list)
lambda_solve_tie_randomly = lambda list: solve_tie_randomly(list)

VALID_TIE_SOLVERS = {'alphabetic', 'random'}
TIE_SOLVERS = {
    'alphabetic': lambda_solve_tie_alphabetically,
    'random': lambda_solve_tie_randomly}


def solve_tie_alphabetically(list):
    return sorted(list)


def solve_tie_randomly(list):
    shuffle(list)
    if len(list) > 1: print(list)
    return list


def obtain_raw_players(players_path):
    raw_players = []

    with open(players_path, 'r') as players_file:
        reader = csv.reader(players_file)
        for row in reader:
            raw_players.append(row)

    return raw_players


def obtain_players(players_names, preferences):
    players = []
    players_dict = {}

    for player_name in players_names:
        new_player = SimplePerson(player_name)

        players_dict[player_name] = new_player
        players.append(new_player)

    for players_name in players_names:
        set_preferences_for_player(players_name, preferences, players_dict)

    print(players)

    return players


def set_preferences_for_player(player_name, preferences, players_dict):

    player_preferences = preferences[player_name]
    player_preferences_as_persons = list(map(lambda x: players_dict[x], player_preferences))

    player = players_dict[player_name]
    player.set_preferences(player_preferences_as_persons)



def obtain_tied_preferences(raw_players):
    players_dict = {}

    for raw_player in raw_players:
        player_name = raw_player[1]
        new_player = Person(player_name)

        players_dict[player_name] = new_player

    for raw_player in raw_players:
        player_name = raw_player[1]
        players_dict[player_name] = get_tied_preferences(raw_player)

    return players_dict


def get_tied_preferences(raw_player):

    grouped_preferences = get_grouped_preferences_of_raw_player_by_score(raw_player)

    tied_preferences: List[List[Any]] = []

    for score, person in grouped_preferences:
        players_per_score = list(map(lambda x: x[0], person))

        tied_preferences.append(players_per_score)

    return tied_preferences


def get_grouped_preferences_of_raw_player_by_score(raw_player):

    preferences_path = raw_player[2]
    preferences = []

    with open(preferences_path, 'r') as preferences_file:
        reader = csv.reader(preferences_file)
        for row in reader:
            preferences.append(row)

    sorted_preferences = sorted(preferences, key=lambda x: x[1], reverse=True)

    return groupby(sorted_preferences, lambda x: x[1])


def solve_tied_preferences(tied_preferences, tie_solver_name):

    preferences = {}

    for player_name, player_tied_preferences in tied_preferences.items():
        tie_solver = TIE_SOLVERS[tie_solver_name]
        player_preferences = flatten(list(map(lambda x: tie_solver(x), player_tied_preferences)))

        preferences[player_name] = player_preferences

    return preferences


if __name__ == '__main__':

    assert len(sys.argv) == 3, 'Two parameters are required.'

    number_of_players = int(sys.argv[1])
    assert number_of_players % 2 == 0, 'There must be a pair amount of players.'

    players_path = sys.argv[2]

    raw_players = obtain_raw_players(players_path)

    assert number_of_players == len(raw_players), \
        'In the players file there must be the same number of players as passed in parameters.'

    tied_preferences = obtain_tied_preferences(raw_players)
    print(tied_preferences)

    preferences = solve_tied_preferences(tied_preferences, 'alphabetic')
    print(preferences)
    print()

    players_names = list(map(lambda x: x[1], raw_players))

    players = obtain_players(players_names, preferences)

    print('API Validation')
    print('Players: ' + str(players))
    print()
    for p in players:
        print(p.get_preferred())
    print()

    half = int(number_of_players / 2)
    best_half = players[:half]
    worst_half = players[half:]

    print(best_half)
    print(worst_half)

    #
    pairs = gale_shapley(best_half)
    print()
    print('The matches for the tournament are:')
    for pair in pairs:
        final_pair = tuple(map(lambda x: x.name, pair))
        print('\t' + str(final_pair))
    print()
