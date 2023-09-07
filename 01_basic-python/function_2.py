import math


def distance(x, y):
    s = 0
    for i, j in zip(x, y):
        s += (i-j)**2
    d = math.sqrt(s)
    return d


p = [2, 3, -1]
q = [4, 1, -2]

print(distance(p, q))
