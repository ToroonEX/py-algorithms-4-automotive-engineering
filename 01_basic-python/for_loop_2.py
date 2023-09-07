a = {"force": [0, 10, 15, 30, 45], "distance": [2.5, 3.5, 6.0, -3.0, 8.1]}

s = 0
for i, j in zip(a["force"], a["distance"]):
    s += i*j
    print("Produkt:", i*j)
print("Summe:", s)
