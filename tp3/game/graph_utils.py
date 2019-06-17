from typing import Dict, Any, Union
import math

from graph import DirectedGraph


def start(graph, group, element):
    for item in graph.get_nodes():
        group[item] = element


# It has to be a connected graph.
def bfs(graph, s):
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
        u = queue.pop(0)
        adjacents = graph.get_adjacents(u)

        for w in adjacents:
            if visited[w] == math.inf:
                w_distance = visited[u] + 1

                visited[w] = w_distance
                parents[w] = u

                if w_distance not in distances:
                    distances[w_distance] = [w]
                else:
                    distances[w_distance].append(w)

                queue.append(w)

    return parents, distances


def ford_fulkerson(graph, source, sink):
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

