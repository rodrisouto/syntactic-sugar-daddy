class StructList:

    def __init__(self, source_list):
        self._inner_list = source_list

    def __len__(self):
        return self._inner_list.__len__()

    def __iter__(self):
        return self._inner_list.__iter__()

    def append(self, e):
        return self._inner_list.append(e)

    def pop(self, pos=None):
        if pos is None:
            return self._inner_list.pop()
        else:
            return self._inner_list.pop(pos)


class StructArray:

    def __init__(self, source_list):
        self._inner_list = source_list

    def __len__(self):
        return self._inner_list.__len__()

    def __getitem__(self, key):
        return self._inner_list.__getitem__(key)

    def __setitem__(self, key, value):
        return self._inner_list.__setitem__(key, value)

    def append(self, e):
        return self._inner_list.append(e)

    def pop(self):
        return self._inner_list.pop()
