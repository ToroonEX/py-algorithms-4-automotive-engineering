import math


def distance(x, y):
    a=[0,0,0]
    for i in range(3):
        a[i] = (x[i]-y[i])**2
    lsg=math.sqrt(a[0]+a[1]+a[2])
    return lsg


x = [2, 3, -1]
y = [4, 1, -2]

print(distance(x, y))
