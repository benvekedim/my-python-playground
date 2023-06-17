import matplotlib.pyplot as plt
import numpy as np

data = np.array([241, 3, 46, 49, 90, 87, 24, 50, 21, 56])
plt.hist(data, bins=10)
plt.show()
