from binary_search_tree import BST
from heap import *


class Person:
    def __init__(self, name, entry, exit):
        self.name = name
        self.entry = entry
        self.exit = exit

    def shares_time_with(self, other_person):
        return self.exit >= other_person.entry

    def minutes_shared_with(self, other_person):
        return self.exit - other_person.entry

    def exits_at_same_time(self, other_person):
        return self.exit == other_person.exit

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.entry < other.entry


class SuspectGroup:
    def __init__(self, suspects, time):
        self.suspects = suspects
        self.time = time

    def __str__(self):
        return str(self.suspects)[1:-1] + ", " + str(self.time)

    def __repr__(self):
        return str(self)


def append_if_are_suspects(suspects, people_inside, next_to_leave):
    if 4 < len(people_inside) <= 10:
        shared_minutes = next_to_leave.minutes_shared_with(people_inside.find_max())
        if 40 <= shared_minutes <= 120:
            s = []
            for person in people_inside:
                s.append(person)
            suspects.append(SuspectGroup(s, shared_minutes))


# param: list of people ordered by entry time
def find_suspects(people):
    people_inside = BST()
    # min heap (ordered by exit time)
    building = Heap(key=lambda person: person.exit)
    # list of SuspectGroups
    suspects = []
    for person in people:
        next_to_leave = building.top()
        while next_to_leave is not None and not next_to_leave.shares_time_with(person):
            same_time = [building.pop()]
            while building.top() is not None and next_to_leave.exits_at_same_time(building.top()):
                same_time.append(building.pop())
            append_if_are_suspects(suspects, people_inside, next_to_leave)
            for next in same_time:
                people_inside.remove(next)
            next_to_leave = building.top()
        people_inside.insert(person)
        building.push(person)

    while len(people_inside) > 4:
        next_to_leave = [building.pop()]
        while building.top() is not None and next_to_leave[0].exits_at_same_time(building.top()):
            next_to_leave.append(building.pop())
        append_if_are_suspects(suspects, people_inside, next_to_leave[0])
        for next in next_to_leave:
            people_inside.remove(next)
    return suspects
