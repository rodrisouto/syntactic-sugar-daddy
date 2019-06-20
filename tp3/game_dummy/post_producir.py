#!/usr/bin/env python3

import os
import sys

sys.path.append("../utils")

import game_utils


def replace_temps(player_no):
    os.rename(game_utils.get_empire_temp_filename(player_no), game_utils.get_empire_filename(player_no))
    os.rename(game_utils.get_harvest_temp_filename(player_no), game_utils.get_harvest_filename(player_no))


def main():
    replace_temps(1)
    replace_temps(2)


if __name__ == '__main__':
    main()