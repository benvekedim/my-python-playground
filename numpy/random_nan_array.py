import numpy as np

arr = np.empty((100, 100, 2))
arr[np.random.randint(100, size=(10, 2)), :, :] = np.nan

print(arr)
