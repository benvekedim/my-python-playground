import pandas as pd

# Örnek bir DataFrame oluştur
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Sütun sırasını değiştir
df = df.reindex(columns=['C', 'A', 'B'])

# Yeni DataFrame'i yazdır
print(df)
