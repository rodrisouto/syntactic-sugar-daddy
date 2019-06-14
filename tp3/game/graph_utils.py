from graph import DirectedGraph


def start(graph, group, element):
    for item in graph:
        group[item] = element


def BFS(graph, s, t, parent):
    visited = {}
    start(graph, visited, False)
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        adjacents = graph.get_adjacents(u)
        for w in adjacents:
            if not visited[w]:
                queue.append(w)
                visited[w] = True
                parent[w] = u

    return visited[t]


def FordFulkerson(graph, source, sink):
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
        while (v != source):
            u = parent[v]
            self.graph[u][v] -= path_flow
            self.graph[v][u] += path_flow
            v = parent[v]

    return max_flow

