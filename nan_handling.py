from sklearn.impute import SimpleImputer
import numpy as np

# Örnek veri oluşturma
arr = np.empty((100, 100, 2))
arr[np.random.randint(100, size=(10, 2)), :, :] = np.nan

# arr'ın kopyasını oluşturma
arr_copy = np.copy(arr)

# SimpleImputer nesnesi oluşturma
imputer = SimpleImputer(strategy='constant', fill_value=0)

# Döngü ile NaN değerleri 0 ile doldurma
for i in range(arr_copy.shape[0]):
    arr_copy[i:i+1, :, :] = imputer.fit_transform(np.squeeze(arr_copy[i:i+1, :, :]))
    
print(arr)
print(arr_copy)

#NaN değer kontrolü
nan_indices = np.argwhere(np.isnan(arr_copy))
print(nan_indices)
