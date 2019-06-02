import sys
from typing import List, Any

from city import City
from graph import DirectedGraph


def resolve_routes(world, routes_filename):

    routes_str = read_from_file(routes_filename)

    for route_str in routes_str.split('\n'):
        route_vec = route_str.split(',')
        capacity = int(route_vec[2])
        world.add_edge(route_vec[0], route_vec[1], capacity)


def resolve_cities(cities_filename):

    cities = []
    cities_str = read_from_file(cities_filename)

    for city_str in cities_str.split('\n'):  # format: 'CityName,Spices'
        city_vec = city_str.split(',')
        city = City(city_vec[0], int(city_vec[1]))
        cities.append(city)

    return cities


def read_from_file(filename):

    with open(filename, 'r') as file:
        return file.read()


def load_board(cities_filename, routes_filename):

    board = DirectedGraph()

    cities: List[City] = resolve_cities(cities_filename)

    for city in cities:
        board.add_node(city.get_name())

    resolve_routes(board, routes_filename)

    return board


def main():

    cities_filename = sys.argv[1]
    routes_filename = sys.argv[2]

    board = load_board(cities_filename, routes_filename)

    print(board.get_nodes())
    print(board.get_edges())


if __name__ == '__main__':
    main()
