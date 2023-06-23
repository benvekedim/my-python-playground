import pandas as pd

# Örnek bir DataFrame oluştur
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Sütun adlarını değiştir
df = df.rename(columns={'B': 'Yeni Ad'})

# Yeni DataFrame'i yazdır
print(df)
