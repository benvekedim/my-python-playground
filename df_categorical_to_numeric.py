# Örnek bir DataFrame oluştur
import pandas as pd

df = pd.DataFrame({'Kategorik Kolon': ["H", "L", "L", "H", "H", "L"]})

# "H" değerini 1'e, "L" değerini 0'a dönüştür
df['Sayısal Kolon'] = df['Kategorik Kolon'].map({'H': 1, 'L': 0})

# Yeni DataFrame'i yazdır
print(df)
