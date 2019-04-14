def gale_shapley(men):
    pairs = set()
    while len(men):
        man = men.pop()
        woman = man.pop_preferred()
        if woman.is_free():
            woman.engage(man)
            man.engage(woman)
            pairs.add((man, woman))
        else:
            if woman.prefers(man):
                pairs.remove((woman.get_partner(), man))
                ex = woman.release()
                ex.free()
                men.append(ex)
                woman.engage(man)
                man.engage(woman)
                pairs.add((man, woman))
    return pairs
