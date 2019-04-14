
def gale_shapley(men: list):
    pairs = set()
    while len(men):
        man = men.pop(0)
        woman = man.pop_preferred()
        print(woman)
        if woman.is_free():
            woman.engage(man)
            man.engage(woman)
            pairs.add((man, woman))
        else:
            if woman.prefers(man):
                ex = woman.release()
                pairs.remove((ex, woman))
                ex.release()
                men.append(ex)
                woman.engage(man)
                man.engage(woman)
                pairs.add((man, woman))

        if man.can_propose():
            men.append(man)
    return pairs
