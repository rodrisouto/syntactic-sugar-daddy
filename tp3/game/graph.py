from typing import Dict, Any, Set


class Graph:
    _edges: Set[Any]
    _adjacencies: Dict[Any, Dict[Any, Any]]

    def __init__(self):
        self._adjacencies = {}
        self._edges = set()

    def __contains__(self, v):
        return v in self._adjacencies

    def __getitem__(self, key):  # THIS IS DONE SO THAT IT RETURNS THE SAME OBJECT THAT WAS PUT IN THE GRAPH AS KEY.
        if key not in self:
            return None
        for w in self._adjacencies[key]:
            for u in self._adjacencies[w]:
                if u == key:
                    return u
        for v in self._adjacencies:
            if v == key:
                return v

    def __setitem__(self, key):
        if key in self._adjacencies:
            adyacentes = self._adjacencies.pop(key)
            self._adjacencies[key] = adyacentes
        else:
            self._adjacencies[key] = {}

    def add_edge(self, v, w, arista) -> bool:
        if v not in self or w not in self:
            return False
        if v == w:
            return False
        if self.are_adjacent(v, w):
            return False
        self._adjacencies[v][w] = arista
        self._adjacencies[w][v] = arista
        self._edges.add((v, w, arista))
        return True

    def remove_edge(self, v, w):
        if v not in self or w not in self:
            return None
        if w not in self._adjacencies[v]:
            return None
        self._adjacencies[v].pop(w)
        edge = self._adjacencies[w].pop(v)
        try:
            self._edges.remove((v, w, edge))
        except:
            self._edges.remove((w, v, edge))
        return edge

    def add_node(self, v) -> bool:
        if v in self:
            return False
        self._adjacencies[v] = {}
        return True

    def remove_node(self, v) -> bool:
        if v not in self:
            return False
        adjacents = self._adjacencies[v].keys()
        for w in adjacents:
            self._adjacencies[w].pop(v)
        self._adjacencies.pop(v)
        return True

    def get_adjacents(self, v):
        if v not in self:
            return []
        return self._adjacencies[v].keys()

    def are_adjacent(self, v, w):
        if v == w:
            return False
        if v not in self or w not in self:
            return False
        if w in self._adjacencies[v]:
            return True
        else:
            return False

    def get_edges(self):
        return self._edges

    def see_edge(self, v, w):
        if v not in self or w not in self:
            return None
        if w not in self._adjacencies[v]:
            return None
        return self._adjacencies[v][w]

    def get_nodes(self):
        return self._adjacencies.keys()

    def amount_of_nodes(self):
        return len(self._adjacencies)


class DirectedGraph:
    _edges: Set[Any]
    _adjacencies: Dict[Any, Dict[Any, Any]]

    def __init__(self):
        self._adjacencies = {}
        self._edges = set()

    def __contains__(self, v):
        return v in self._adjacencies

    def __getitem__(self, key):  # THIS IS DONE SO THAT IT RETURNS THE SAME OBJECT THAT WAS PUT IN THE GRAPH AS KEY.
        if key not in self:
            return None
        for w in self._adjacencies[key]:
            for u in self._adjacencies[w]:
                if u == key:
                    return u
        for v in self._adjacencies:
            if v == key:
                return v

    def __setitem__(self, key):
        if key in self._adjacencies:
            adyacentes = self._adjacencies.pop(key)
            self._adjacencies[key] = adyacentes
        else:
            self._adjacencies[key] = {}

    def add_edge(self, v, w, arista) -> bool:
        if v not in self._adjacencies.keys():
            raise Exception("Node {} is not in the graph.".format(v))
        if w not in self:
            raise Exception("Node {} is not in the graph.".format(w))
        if v == w:
            raise Exception('Nodes {} and {} are the same, reflexive edges are not allowed.'.format(v, w))
        if self.are_adjacent(v, w):
            raise Exception('Nodes {} or {} are already connected.'.format(v, w))

        self._adjacencies[v][w] = arista
        self._edges.add((v, w, arista))

    def remove_edge(self, v, w):
        if v not in self or w not in self:
            return None
        if w not in self._adjacencies[v]:
            return None
        self._adjacencies[v].pop(w)
        edge = self._adjacencies[w].pop(v)
        try:
            self._edges.remove((v, w, edge))
        except:
            self._edges.remove((w, v, edge))
        return edge

    def add_node(self, v) -> bool:
        if v in self:
            raise Exception("Node {} is already in the graph.".format(v))
        self._adjacencies[v] = {}
        return True

    def remove_node(self, v) -> bool:
        if v not in self:
            raise Exception("Node {} is not in the graph.".format(v))
        adjacents = self._adjacencies[v].keys()
        for w in adjacents:
            self._adjacencies[w].pop(v)
        self._adjacencies.pop(v)
        return True

    def get_adjacents(self, v):
        if v not in self:
            raise Exception("Node {} is not in the graph.".format(v))
        return self._adjacencies[v].keys()

    def are_adjacent(self, v, w):
        if v == w:
            return False
        if v not in self:
            raise Exception("Node {} is not in the graph.".format(v))
        if w not in self:
            raise Exception("Node {} is not in the graph.".format(w))
        if w in self._adjacencies[v]:
            return True
        else:
            return False

    def get_edges(self):
        return self._edges

    def see_edge(self, v, w):
        if v not in self:
            raise Exception("Node {} is not in the graph.".format(v))
        if w not in self:
            raise Exception("Node {} is not in the graph.".format(w))
        if w not in self._adjacencies[v]:
            return None
        return self._adjacencies[v][w]

    def get_nodes(self):
        return self._adjacencies.keys()

    def amount_of_nodes(self):
        return len(self._adjacencies)


