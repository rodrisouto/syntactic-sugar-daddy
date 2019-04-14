def is_stable(pairs):
    for i in pairs:
        x = i[0]
        for j in pairs:
            if x != j[0]:
                if x.prefers(j[1]) and j[1].prefers(x):
                     return False
    return True

