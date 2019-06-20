#!/usr/bin/env python3

from typing import Dict, Any
import math
from copy import copy

from graph import DirectedGraph


def start(graph, group, element):

    for item in graph.get_nodes():
        group[item] = element


def bfs(graph, s, f_valid_edge=lambda x, y: True):

    visited: Dict[Any, int] = {}
    parents: Dict[Any, Any] = {}
    distances: Dict[int, Any] = {}
    queue = []

    start(graph, visited, math.inf)
    start(graph, parents, None)

    visited[s] = 0
    parents[s] = None
    distances[0] = [s]
    queue.append(s)

    while len(queue) != 0:
        v = queue.pop(0)

        adjacents = graph.get_adjacents(v)

        for w in adjacents:
            if f_valid_edge(v, w) and visited[w] == math.inf:
                w_distance = visited[v] + 1

                visited[w] = w_distance
                parents[w] = v

                if w_distance not in sorted(distances.keys()):
                    distances[w_distance] = [w]
                else:
                    distances[w_distance].append(w)

                queue.append(w)

    return parents, distances


def invert_graph(original_graph):

    new_graph = copy_directed_graph(original_graph)
    original_edges = copy(new_graph.get_edges())
    inverted_edges = []

    for edge in original_edges:
        inverted_edges.append((edge[1], edge[0], edge[2]))
        new_graph.remove_edge(edge[0], edge[1])

    for edge in inverted_edges:
        new_graph.add_edge(edge[0], edge[1], edge[2])

    return new_graph


def generate_directed_subgraph(original_graph, nodes_subset) -> DirectedGraph:

    new_graph = DirectedGraph()

    for node in original_graph.get_nodes():
        if node in nodes_subset:
            new_graph.add_node(node)

    for edge in original_graph.get_edges():
        if edge[0] in nodes_subset and edge[1] in nodes_subset:
            new_graph.add_edge(edge[0], edge[1], edge[2])

    return new_graph


def copy_directed_graph(original_graph):

    return generate_directed_subgraph(original_graph, set(original_graph.get_nodes()))


def find_path(parents, v):

    path = []

    while parents[v] is not None:
        path.append(v)
        v = parents[v]

    if parents[path[len(path)-1]] is not None:
        path.append(parents[path[len(path)-1]])

    path.reverse()
    return path


def find_bottleneck(residual_graph, path):

    bottleneck = math.inf

    for i in range(len(path)-1):
        edge = residual_graph.get_edge(path[i], path[i+1])
        if edge < bottleneck:
            bottleneck = edge

    assert bottleneck is not 0

    return bottleneck


def update_edges_ff(graph, path, bottleneck):

    for i in range(len(path)-1):
        src = path[i]
        dst = path[i+1]

        src_dst = graph.get_edge(src, dst) - bottleneck
        graph.remove_edge(src, dst)
        graph.add_edge(src, dst, src_dst)

        dst_src = graph.get_edge(dst, src) + bottleneck
        graph.remove_edge(dst, src)
        graph.add_edge(dst, src, dst_src)

        assert graph.get_edge(src, dst) >= 0


def validate_graph_for_ff(graph, sink):

    assert len(graph.get_adjacents(sink)) is 0

    """
    for edge in graph.get_edges():
        assert not graph.are_adjacents(edge[1], edge[0]), 'Vertices {} and {} are double connected.'.format(edge[0], edge[1])
        """


def add_super_source(resigual_graph, sources, sources_limit):

    super_source = '----super_source----'
    assert super_source not in resigual_graph
    resigual_graph.add_node(super_source)
    list(map(lambda x: resigual_graph.add_edge(super_source, x, sources_limit[x]), sources))
    list(map(lambda x: resigual_graph.add_edge(x, super_source, 0), sources))

    return super_source


def initialize_return_edges(graph, residual_graph):

    for edge in graph.get_edges():
        src = edge[0]
        dst = edge[1]

        residual_graph.add_edge(dst, src, 0)


def calculate_flux(graph, residual_graph, sources, sink):

    flux_to_sink = 0
    for w in residual_graph.get_adjacents(sink):
        flux_to_sink += residual_graph.get_edge(sink, w)

    return flux_to_sink


# Edges must be integers.
def ford_fulkerson(graph, source, sink):

    validate_graph_for_ff(graph)

    assert len(graph.get_nodes()) > 1

    residual_graph = copy_directed_graph(graph)

    initialize_return_edges(graph, residual_graph)

    while True:
        parents, _ = bfs(residual_graph, source, lambda x, y: residual_graph.get_edge(x, y) > 0)
        if parents[sink] is None:
            break

        path = find_path(parents, sink)
        bottleneck = find_bottleneck(residual_graph, path)

        update_edges_ff(residual_graph, path, bottleneck)

    return calculate_flux(graph, residual_graph, [source], sink)


# Edges must be integers.
def ford_fulkerson_multiple_sources(graph, sources, sink):

    validate_graph_for_ff(graph)

    assert len(graph.get_nodes()) > 1

    residual_graph = copy_directed_graph(graph)
    super_source = add_super_source(residual_graph, sources)

    initialize_return_edges(graph, residual_graph)

    while True:
        parents, _ = bfs(residual_graph, super_source, lambda x, y: residual_graph.get_edge(x, y) > 0)
        if parents[sink] is None:
            break

        path = find_path(parents, sink)
        bottleneck = find_bottleneck(residual_graph, path)

        update_edges_ff(residual_graph, path, bottleneck)

    return calculate_flux(graph, residual_graph, sources, sink)


def complex_valid_edge(graph, residual_graph, sources_limit):

    def _complex_valid_edge(v, w) -> bool:
        if residual_graph.get_edge(v, w) <= 0:
            return False

        # If v is not source.
        if v not in sources_limit:
            return True

        flux_from_source = 0
        for u in graph.get_adjacents(v):
            flux_from_source += residual_graph.get_edge(u, v)

        assert flux_from_source <= sources_limit[v], 'v:{} | flux_from_source: {} | sources_limit[v]: {}'.format(v, flux_from_source, sources_limit[v])

        if flux_from_source == sources_limit[v]:
            return False

        return True

    return _complex_valid_edge


def ford_fulkerson_multiple_sources_and_limits(graph, sources, sink, sources_limit: Dict[Any, int]):

    validate_graph_for_ff(graph, sink)
    for source in sources:
        assert source in sources_limit

    if len(graph.get_nodes()) <= 1:
        return 0

    residual_graph = copy_directed_graph(graph)

    super_source = add_super_source(residual_graph, sources, sources_limit)

    initialize_return_edges(graph, residual_graph)

    while True:
        parents, _ = bfs(residual_graph, super_source, lambda x, y: residual_graph.get_edge(x, y) > 0)
        if parents[sink] is None:
            break

        path = find_path(parents, sink)
        bottleneck = find_bottleneck(residual_graph, path)

        update_edges_ff(residual_graph, path, bottleneck)

    return calculate_flux(graph, residual_graph, sources, sink)


def generate_directed_graph_without_double_connections(original_graph, s):

    new_graph = copy_directed_graph(original_graph)
    visited = set()
    queue = []

    visited.add(s)
    queue.append(s)

    while len(queue) != 0:
        v = queue.pop(0)
        adjacents = new_graph.get_adjacents(v)

        for w in adjacents:
            if new_graph.are_adjacents(w, v):
                new_graph.remove_edge(w, v)

                if w not in visited:
                    visited.add(w)
                    queue.append(w)

    return new_graph


# Graph was taken from this example: https://www.youtube.com/watch?v=Tl90tNtKvxs
def test_ford_fulkerson():

    graph = DirectedGraph()

    graph.add_node('s')
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('t')

    graph.add_edge('s', 'a', 10)
    graph.add_edge('s', 'c', 10)
    graph.add_edge('a', 'b', 4)
    graph.add_edge('a', 'c', 2)
    graph.add_edge('a', 'd', 8)
    graph.add_edge('b', 't', 10)
    graph.add_edge('c', 'd', 9)
    graph.add_edge('d', 'b', 6)
    graph.add_edge('d', 't', 10)

    flux = ford_fulkerson(graph, 's', 't')
    assert flux == 19, 'Flux expected was 19, found: {}'.format(flux)


def test_ford_fulkerson_multiple_sources_one_source():

    graph = DirectedGraph()

    graph.add_node('s')
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('t')

    graph.add_edge('s', 'a', 10)
    graph.add_edge('s', 'c', 10)
    graph.add_edge('a', 'b', 4)
    graph.add_edge('a', 'c', 2)
    graph.add_edge('a', 'd', 8)
    graph.add_edge('b', 't', 10)
    graph.add_edge('c', 'd', 9)
    graph.add_edge('d', 'b', 6)
    graph.add_edge('d', 't', 10)

    flux = ford_fulkerson_multiple_sources(graph, ['s'], 't')
    assert flux == 19, 'Flux expected was 19, found: {}'.format(flux)


def test_ford_fulkerson_multiple_sources_two_sources():

    graph = DirectedGraph()

    graph.add_node('s')
    graph.add_node('s2')
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('t')

    graph.add_edge('s', 'a', 10)
    graph.add_edge('s', 'c', 10)
    graph.add_edge('a', 'b', 4)
    graph.add_edge('a', 'c', 2)
    graph.add_edge('a', 'd', 8)
    graph.add_edge('b', 't', 10)
    graph.add_edge('c', 'd', 9)
    graph.add_edge('d', 'b', 6)
    graph.add_edge('d', 't', 10)

    graph.add_edge('s2', 'b', 5)

    flux = ford_fulkerson_multiple_sources(graph, ['s', 's2'], 't')
    assert flux == 20, 'Flux expected was 19, found: {}'.format(flux)


def test_ford_fulkerson_multiple_sources_one_source_with_limit():

    graph = DirectedGraph()

    graph.add_node('s')
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('t')

    graph.add_edge('s', 'a', 10)
    graph.add_edge('s', 'c', 10)
    graph.add_edge('a', 'b', 4)
    graph.add_edge('a', 'c', 2)
    graph.add_edge('a', 'd', 8)
    graph.add_edge('b', 't', 10)
    graph.add_edge('c', 'd', 9)
    graph.add_edge('d', 'b', 6)
    graph.add_edge('d', 't', 10)

    sources_limit = {'s': 14}

    flux = ford_fulkerson_multiple_sources_and_limits(graph, ['s'], 't', sources_limit)
    assert flux == 14, 'Flux expected was 14, found: {}'.format(flux)


def test_ford_fulkerson_multiple_sources_two_sources_with_limit():

    graph = DirectedGraph()

    graph.add_node('s')
    graph.add_node('s2')
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('t')

    graph.add_edge('s', 'a', 10)
    graph.add_edge('s', 'c', 10)
    graph.add_edge('a', 'b', 4)
    graph.add_edge('a', 'c', 2)
    graph.add_edge('a', 'd', 8)
    graph.add_edge('b', 't', 10)
    graph.add_edge('c', 'd', 9)
    graph.add_edge('d', 'b', 6)
    graph.add_edge('d', 't', 10)

    graph.add_edge('s2', 'b', 5)

    sources_limit = {'s': 14, 's2': 1}

    flux = ford_fulkerson_multiple_sources_and_limits(graph, ['s', 's2'], 't', sources_limit)
    assert flux == 15, 'Flux expected was 15, found: {}'.format(flux)


if __name__ == '__main__':
    """
    test_ford_fulkerson()
    test_ford_fulkerson_multiple_sources_one_source()
    test_ford_fulkerson_multiple_sources_two_sources()
    """
    test_ford_fulkerson_multiple_sources_one_source_with_limit()
    test_ford_fulkerson_multiple_sources_two_sources_with_limit()