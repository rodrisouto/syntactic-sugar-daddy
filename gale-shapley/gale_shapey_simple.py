from people import Person


def gale_shapley_simple(men):
    pairs = set()
    while len(men):
        man = men.pop()
        woman = man.get_preferred()
        if woman.is_free():
            woman.engage(man)
            man.engage(woman)
            pairs.add((man, woman))
        if not woman.is_free():
            if woman.prefers(man):
                pairs.remove((woman.get_partner(), man))
                ex = woman.release()
                ex.free()
                men.append(ex)
                woman.engage(man)
                man.engage(woman)
                pairs.add((man, woman))
    print(pairs)


def gale_shapley():
    w1 = Person("w1")
    w2 = Person("w2")
    m1 = Person("m1")
    m2 = Person("m2")
    w1.set_preferences([m1, m2])
    w2.set_preferences([m2, m1])
    m1.set_preferences([w1, w2])
    m2.set_preferences([w2, w1])
    gale_shapley_simple([m1, m2])


gale_shapley()