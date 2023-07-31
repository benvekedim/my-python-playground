import pandas as pd

# Örnek bir veri seti oluşturalım
data = pd.DataFrame({'renk': ['kırmızı', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'sarı'],
                     'sayi': [10, 20, 30, 40, 50, 60],
                     'kategori': ['A', 'B', 'A', 'C', 'B', 'C']})

# 'renk' ve 'kategori' sütunlarını veri setinden çıkaralım
data = data.drop(['renk', 'kategori'], axis=1)

# Veri setini ekrana yazdıralım
print(data)
