import sys

sys.path.append('../utils/')

from people import Person
from gale_shapley import gale_shapley
from stable_matching import is_stable


def gale_shapley_one_posible_solution():
    w1 = Person("w1")
    w2 = Person("w2")
    m1 = Person("m1")
    m2 = Person("m2")
    w1.set_preferences([m1, m2])
    w2.set_preferences([m2, m1])
    m1.set_preferences([w1, w2])
    m2.set_preferences([w2, w1])
    assert (gale_shapley([m1, m2]) == {(m1, w1), (m2, w2)})
    w1.set_preferences([m1, m2])
    w2.set_preferences([m2, m1])
    m1.set_preferences([w1, w2])
    m2.set_preferences([w2, w1])
    assert (is_stable({(m1, w1), (m2, w2)}))


def gale_shapley_prefers():
    w1 = Person("w1")
    w2 = Person("w2")
    m1 = Person("m1")
    m2 = Person("m2")
    w1.set_preferences([m2, m1])
    w2.set_preferences([m1, m2])
    m1.set_preferences([w1, w2])
    m2.set_preferences([w1, w2])
    assert (gale_shapley([m1, m2]) == {(m1, w2), (m2, w1)})
    w1.set_preferences([m2, m1])
    w2.set_preferences([m1, m2])
    m1.set_preferences([w1, w2])
    m2.set_preferences([w1, w2])
    assert (is_stable({(m2, w1), (m1, w2)}))

def gale_shapley_two_stables_first():
    w1 = Person("w1")
    w2 = Person("w2")
    m1 = Person("m1")
    m2 = Person("m2")
    w1.set_preferences([m2, m1])
    w2.set_preferences([m1, m2])
    m1.set_preferences([w1, w2])
    m2.set_preferences([w2, w1])
    assert (gale_shapley([m1, m2]) == {(m1, w1), (m2, w2)})
    w1.set_preferences([m2, m1])
    w2.set_preferences([m1, m2])
    m1.set_preferences([w1, w2])
    m2.set_preferences([w2, w1])
    assert (is_stable({(m1, w1), (m2, w2)}))


def gale_shapley_two_stables_second():
    w1 = Person("w1")
    w2 = Person("w2")
    m1 = Person("m1")
    m2 = Person("m2")
    w1.set_preferences([m2, m1])
    w2.set_preferences([m1, m2])
    m1.set_preferences([w1, w2])
    m2.set_preferences([w2, w1])
    assert (gale_shapley([w1, w2]) == {(w2, m1), (w1, m2)})
    w1.set_preferences([m2, m1])
    w2.set_preferences([m1, m2])
    m1.set_preferences([w1, w2])
    m2.set_preferences([w2, w1])
    assert (is_stable({(w2, m1), (w1, m2)}))


def gale_shapley_with_3():
    w1 = Person("w1")
    w2 = Person("w2")
    w3 = Person("w3")
    m1 = Person("m1")
    m2 = Person("m2")
    m3 = Person("m3")
    w1.set_preferences([m2, m1, m3])
    w2.set_preferences([m3, m2, m1])
    w3.set_preferences([m1, m3, m2])
    m1.set_preferences([w2, w1, w3])
    m2.set_preferences([w3, w2, w1])
    m3.set_preferences([w1, w3, w2])
    assert (gale_shapley([m1, m2, m3]) == {(m1, w2), (m2, w3), (m3, w1)})
    w1.set_preferences([m2, m1, m3])
    w2.set_preferences([m3, m2, m1])
    w3.set_preferences([m1, m3, m2])
    m1.set_preferences([w2, w1, w3])
    m2.set_preferences([w3, w2, w1])
    m3.set_preferences([w1, w3, w2])
    assert (is_stable({(m1, w2), (m2, w3), (m3, w1)}))


gale_shapley_one_posible_solution()
gale_shapley_prefers()
gale_shapley_one_posible_solution()
gale_shapley_two_stables_first()
gale_shapley_two_stables_second()
gale_shapley_with_3()
