
import heapq


class Heap(object):
    def __init__(self, initial=None, key=lambda x: x):
        self.id = 0
        self.key = key
        if initial:
            self._data = [(key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), self.id, item))
        self.id += 1

    def pop(self):
        return heapq.heappop(self._data)[2]

    def top(self):
        return self._data[0][2] if len(self._data) > 0 else None
