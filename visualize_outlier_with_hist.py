import matplotlib.pyplot as plt
import numpy as np

data = np.array([241, 3, 46, 49, 90, 87, 24, 50, 21, 56])
plt.hist(data, bins=10)
plt.show()

#manuel bins parametresi bulma

iqr = np.percentile(data, 75) - np.percentile(data, 25)
bin_width = 2 * iqr / (len(data) ** (1/3))
bins = int((np.max(data) - np.min(data)) / bin_width)
bins

plt.hist(data, bins=5)
plt.show()
