from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

# Örnek bir veri seti oluşturalım
data = pd.DataFrame({'renk': ['kırmızı', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'sarı']})

# OrdinalEncoder nesnesi oluşturalım
encoder = OrdinalEncoder()

# 'renk' sütununu ordinal encoding işlemine tabi tutalım
data['renk_encoded'] = encoder.fit_transform(data[['renk']])

print(data)
