#!/usr/bin/env python3

from typing import Dict, Any
import math

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

                if w_distance not in distances:
                    distances[w_distance] = [w]
                else:
                    distances[w_distance].append(w)

                queue.append(w)

    return parents, distances


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


def find_bottleneck(graph, path):

    bottleneck = math.inf

    for i in range(len(path)-1):
        edge = graph.get_edge(path[i], path[i+1])
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


def validate_graph_for_ff(graph):

    for edge in graph.get_edges():
        assert not graph.are_adjacents(edge[1], edge[0]), 'Vertices {} and {} are double connected.'.format(edge[0], edge[1])


def add_super_source(resigual_graph, sources):

    super_source = '----super_source----'
    assert super_source not in resigual_graph
    resigual_graph.add_node(super_source)
    list(map(lambda x: resigual_graph.add_edge(super_source, x, math.inf), sources))
    list(map(lambda x: resigual_graph.add_edge(x, super_source, 0), sources))

    return super_source


def initialize_return_edges(graph, residual_graph):

    for edge in graph.get_edges():
        src = edge[0]
        dst = edge[1]

        residual_graph.add_edge(dst, src, 0)


def calculate_flux(graph, residual_graph, sources, sink):

    flux_from_source = 0
    for source in sources:
        for w in graph.get_adjacents(source):
            flux_from_source += residual_graph.get_edge(w, source)

    flux_to_sink = 0
    for w in residual_graph.get_adjacents(sink):
        flux_to_sink += residual_graph.get_edge(sink, w)

    assert flux_from_source == flux_to_sink, '{} {}'.format(flux_from_source, flux_to_sink)

    return flux_from_source


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
        if v not in sources_limit:
            return True

        flux_from_source = 0
        for u in graph.get_adjacents(v):
            flux_from_source += flux_from_source + residual_graph.get_edge(u, v)

    return _complex_valid_edge


def ford_fulkerson_multiple_sources_2(graph, sources, sink, sources_limit: Dict[Any, int]):

    validate_graph_for_ff(graph)
    for source in sources:
        assert source in sources_limit

    assert len(graph.get_nodes()) > 1

    residual_graph = copy_directed_graph(graph)
    super_source = add_super_source(residual_graph, sources)

    initialize_return_edges(graph, residual_graph)

    while True:
        parents, _ = bfs(residual_graph, super_source, complex_valid_edge(graph, residual_graph, sources_limit))
        if parents[sink] is None:
            break

        path = find_path(parents, sink)
        bottleneck = find_bottleneck(residual_graph, path)

        update_edges_ff(residual_graph, path, bottleneck)

    return calculate_flux(graph, residual_graph, sources, sink)


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

    sources_limit = {'s': 19}

    flux = ford_fulkerson_multiple_sources_2(graph, ['s'], 't', sources_limit)
    assert flux == 19, 'Flux expected was 19, found: {}'.format(flux)

if __name__ == '__main__':
    test_ford_fulkerson()
    test_ford_fulkerson_multiple_sources_one_source()
    test_ford_fulkerson_multiple_sources_two_sources()
    test_ford_fulkerson_multiple_sources_one_source_with_limit()