a = {"scale": 3.6, "speed": [0., 15., 22., 30.], "label": "Scaled speed"}

for i in range(len(a["speed"])):
    print(a["scale"]*a["speed"][i])
