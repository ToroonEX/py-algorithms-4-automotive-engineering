from statistics import stdev


def standardabweichung(list):
    lsg = stdev(list)
    return lsg


list_1 = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
print(standardabweichung(list_1))
