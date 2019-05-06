

class EmptyStackException(Exception):
    pass


class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if self.is_empty():
            raise EmptyStackException()
        return self.data[-1]

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackException()
        return self.data.pop()

    def __len__(self):
        return len(self.data)
