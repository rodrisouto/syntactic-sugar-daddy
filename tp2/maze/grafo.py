from typing import Dict, Any, Set


class Grafo:
    _aristas: Set[Any]
    _adyacencias: Dict[Any, Dict[Any, Any]]

    def __init__(self):
        self._adyacencias = {}
        self._aristas = set()

    def __contains__(self, v):
        return v in self._adyacencias

    def __getitem__(self, key):  # ESTO LO HACEMOS PARA QUE SE DEVUELVA EL MISMO OBJETO QUE SE TIENE EN EL GRAFO
        if key not in self:
            return None
        for w in self._adyacencias[key]:
            for u in self._adyacencias[w]:
                if u == key:
                    return u
        for v in self._adyacencias:
            if v == key:
                return v

    def __setitem__(self, key):
        if key in self._adyacencias:
            adyacentes = self._adyacencias.pop(key)
            self._adyacencias[key] = adyacentes
        else:
            self._adyacencias[key] = {}

    def agregar_arista(self, v, w, arista) -> bool:
        if v not in self or w not in self:
            return False
        if v == w:
            return False
        if self.son_adyacentes(v, w):
            return False
        self._adyacencias[v][w] = arista
        self._adyacencias[w][v] = arista
        self._aristas.add((v, w, arista))
        return True

    def borrar_arista(self, v, w):
        if v not in self or w not in self:
            return None
        if w not in self._adyacencias[v]:
            return None
        self._adyacencias[v].pop(w)
        arista = self._adyacencias[w].pop(v)
        try:
            self._aristas.remove((v, w, arista))
        except:
            self._aristas.remove((w, v, arista))
        return arista

    def agregar_vertice(self, v) -> bool:
        if v in self:
            return False
        self._adyacencias[v] = {}
        return True

    def borrar_vertice(self, v) -> bool:
        if v not in self:
            return False
        adyacentes = self._adyacencias[v].keys()
        for w in adyacentes:
            self._adyacencias[w].pop(v)
        self._adyacencias.pop(v)
        return True

    def obtener_adyacentes(self, v):
        if v not in self:
            return []
        return self._adyacencias[v].keys()

    def son_adyacentes(self, v, w):
        if v == w:
            return False
        if v not in self or w not in self:
            return False
        if w in self._adyacencias[v]:
            return True
        else:
            return False

    def obtener_aristas(self):
        return self._aristas

    def ver_arista(self, v, w):
        if v not in self or w not in self:
            return None
        if w not in self._adyacencias[v]:
            return None
        return self._adyacencias[v][w]

    def obtener_vertices(self):
        return self._adyacencias.keys()

    def cant_vertices(self):
        return len(self._adyacencias)
