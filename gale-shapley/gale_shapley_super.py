from people import Person

def gale_shapley_super_stable(men, women):
    pairs = set()
    while len(men):
        man = men.pop()
        preferred_women = man.get_preferred()
        for woman in preferred_women:
            woman.engage(man)
            man.engage(woman)
            pairs.add((man, woman))
            rejected = woman.get_rejected(man)
            for i in rejected:
                i.free(woman)
                pairs.remove((i, woman))
        for woman in women:
            if woman.is_multiply_engaged():
                partners = woman.get_partners()
                for i in partners:
                    pairs.remove((i, woman))
    print(pairs)


def run():
    w1 = Person("w1")
    w2 = Person("w2")
    m1 = Person("m1")
    m2 = Person("m2")
    w1.set_preferences([[m2], [m1]])
    w2.set_preferences([[m2], [m1]])
    m1.set_preferences([[w1], [w2]])
    m2.set_preferences([[w1, w2]])
    gale_shapley_super_stable([m1, m2], [w1, w2])

run()





