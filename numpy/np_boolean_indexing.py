import numpy as np

# Örnek bir ndarry oluştur
arr = np.array(["a", "b", "c"])

# "a" elemanını silmeden "b" ve "c" elemanlarını seç
new_arr = arr[arr != "a"]

# Yeni ndarry'i yazdır
print(new_arr)
