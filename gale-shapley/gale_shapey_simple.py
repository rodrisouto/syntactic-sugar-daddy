
def gale_shapley_simple(men, women):
#Initially all m ∈ M and w ∈ W are free
    free_men = men
    while not free_men.empty():
        man = free_men.pop()
        woman = man.get_prefered()
        if woman.free():
            woman.engage(man)
            man.engage(woman)
        if woman.engaged():
            if not woman.prefers(man):
                #m is free
            else:
                woman.release().free()
                woman.engage(man)
                man.engage(woman)
        return S
