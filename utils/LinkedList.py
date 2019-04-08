
class Node:
    def __init__(self, n):
        self.number = n
        self.next = None


class LinkedListIterator:
    def __init__(self, linked_list):
        self.curr = linked_list.head

    def __next__(self):
        n = self.curr
        if n is None:
            raise StopIteration
        self.curr = self.curr.next
        return n.number


class LinkedList:
    def __init__(self, numbers):
        self.head = Node(numbers[0])
        self.len = len(numbers)
        prev = self.head
        for n in range(1, len(numbers)):
            prev.next = Node(numbers[n])
            prev = prev.next

    def __len__(self):
        return self.len

    def __iter__(self):
        return LinkedListIterator(self)
