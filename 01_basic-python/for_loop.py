dic = {"force": [0, 10, 15, 30, 45], "distance": [2.5, 3.5, 6.0, -3.0, 8.1]}
summe = 0

for i in range(5):
    summe = summe+dic["force"][i]*dic["distance"][i]

print(summe)
