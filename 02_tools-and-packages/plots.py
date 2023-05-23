from matplotlib import pyplot as plt
import numpy as np


y = [np.random.normal(0, 0.1, 1500)]
plt.hist(y, bins=40)
plt.xlabel("Wert")
plt.ylabel("Wahrscheinlichkeit")
plt.title("Gaussverteilung")
plt.show()

