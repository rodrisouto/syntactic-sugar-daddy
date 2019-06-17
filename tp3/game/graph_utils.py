#!/usr/bin/env python3

from typing import Dict, Any
import math

from graph import DirectedGraph


def start(graph, group, element):

    for item in graph.get_nodes():
        group[item] = element


def bfs(graph, s, f_valid_edge=lambda x: True):

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
            if f_valid_edge(graph.get_edge(v, w)) and visited[w] == math.inf:
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


def ford_fulkerson_pre(graph, source, sink):
    parent = {}
    start(graph, parent, None)
    max_flow = 0
    path_flow = 1000000

    while BFS(graph, source, sink, parent):

        while sink != source:
            path_flow = min(path_flow, ) #necesito el peso de la arista
            sink = parent[sink]

        max_flow += path_flow

        # update residual capacities of the edges and reverse edges
        # along the path
        v = sink
        while v != source:
            u = parent[v]
            self.graph[u][v] -= path_flow
            self.graph[v][u] += path_flow
            v = parent[v]

    return max_flow


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


# !!!! def valid_edge_ff(

# !!!! borrar
def get_ff_adjacents(graph, residual_graph, v):

    adjacents_in_graph = list(filter(lambda x: x - residual_graph.get_edge(x, v) > 0, graph.get_adjacents(v)))

    adjacents_in_residual_graph = list(filter(lambda x: residual_graph.get_edge(x, v) > 0, graph.get_adjacents(v)))

    print('adjacents_in_graph {}'.format(adjacents_in_graph))
    print('adjacents_in_residual_graph {}'.format(adjacents_in_residual_graph))

    # return set(adjacents_in_graph +

# !!!! borrar
"""
def bfs_ff(graph, residual_graph, s):

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

        adjacents = get_ff_adjacents(graph, residual_graph, v)

        for w in adjacents:
            if visited[w] == math.inf:
                w_distance = visited[v] + 1

                visited[w] = w_distance
                parents[w] = v

                if w_distance not in distances:
                    distances[w_distance] = [w]
                else:
                    distances[w_distance].append(w)

                queue.append(w)

    return parents, distances
"""


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


# Edges must be integers.
def ford_fulkerson(graph, source, sink):

    assert len(graph.get_nodes()) > 1

    resigual_graph = copy_directed_graph(graph)

    print('nodes: {}'.format(len(resigual_graph.get_nodes())))
    print('edges: {}'.format(len(resigual_graph.get_edges())))

    for edge in graph.get_edges():
        src = edge[0]
        dst = edge[1]

        resigual_graph.add_edge(dst, src, 0)

    i = 0
    while True:
        parents, _ = bfs(resigual_graph, source, lambda x: x > 0)
        print(parents)
        if parents[sink] is None:
            break

        path = find_path(parents, sink)
        print(path)
        bottleneck = find_bottleneck(resigual_graph, path)
        print('bottleneck: {}'.format(bottleneck))

        update_edges_ff(resigual_graph, path, bottleneck)
        print('edges: {}'.format(resigual_graph.get_edges()))
        print()


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

    ford_fulkerson(graph, 's', 't')


if __name__ == '__main__':
    test_ford_fulkerson()
