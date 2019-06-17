import sys
from typing import List, Any

from city import City
from graph import DirectedGraph


def _resolve_routes(world, routes_filename):

    routes_str = _read_from_file(routes_filename)

    for route_str in routes_str.split('\n'):
        if route_str == '':
            continue

        route_vec = route_str.split(',')
        assert len(route_vec) == 3, 'Route does not have 3 elements: {}'.format(route_vec)
        capacity = int(route_vec[2])
        world.add_edge(route_vec[0], route_vec[1], capacity)


def _resolve_cities(cities_filename):

    cities = {}
    cities_str = _read_from_file(cities_filename)

    for city_str in cities_str.split('\n'):  # format: 'CityName,Spices'
        city_vec = city_str.split(',')
        city_name = city_vec[0]
        city = City(city_name, int(city_vec[1]))
        cities[city_name] = city

    return cities


def _read_from_file(filename):

    with open(filename, 'r') as file:
        return file.read()


def load_board(cities_filename, routes_filename):

    board = DirectedGraph()

    cities: dict[str, City] = _resolve_cities(cities_filename)

    for city in cities:
        board.add_node(cities[city].get_name())

    _resolve_routes(board, routes_filename)

    return board, cities


def main():

    cities_filename = sys.argv[1]
    routes_filename = sys.argv[2]

    board, cities = load_board(cities_filename, routes_filename)

    print(board.get_nodes())
    print(board.get_edges())


if __name__ == '__main__':
    main()
