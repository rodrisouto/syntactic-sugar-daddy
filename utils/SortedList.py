
class Node:
    def __init__(self, n):
        self.number = n
        self.next = None

class SortedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def addOrdered(self, number):
        self.len += 1
        if not self.head:
            self.head = Node(number)
            return
        prev = None
        curr = self.head
        while curr and curr.number > number:
            prev = curr
            curr = curr.next
        new = Node(number)
        if prev is None:
            self.head = new
        else:
            prev.next = new
        new.next = curr

    def __len__(self):
        return self.len

    def __repr__(self):
        l = []
        curr = self.head
        while curr:
            l.append(str(curr.number))
            curr = curr.next
        s = "[" + ",".join(l) + "]"
        return s

    def __str__(self):
        return self.__repr__()

    def get(self, index):
        if index >= len(self): raise IndexError
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.number
