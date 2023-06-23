# Örnek bir DataFrame oluştur
import pandas as pd

# df = pd.DataFrame({'Kategorik Kolon': ["H", "L", "L", "H", "H", "L"]})

# "H" değerini 1'e, "L" değerini 0'a dönüştür
# df['Sayısal Kolon'] = df['Kategorik Kolon'].map({'H': 1, 'L': 0})

# Örnek bir DataFrame oluştur
df = pd.DataFrame({'value': [10, 20, 30], 'type': ['H', 'L', 'M']})

# "type" sütunundaki kategorik değerleri sayısal değerlere dönüştür
type_dict = {'H': 1, 'M': 2, 'L': 3}
df['type'] = df['type'].map(type_dict)

# Yeni DataFrame'i yazdır
print(df)
