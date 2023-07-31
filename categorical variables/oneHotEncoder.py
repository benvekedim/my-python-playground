from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Örnek bir veri seti oluşturalım
data = pd.DataFrame({'renk': ['kırmızı', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'sarı']})

# OneHotEncoder nesnesi oluşturalım ve 'renk' sütununu One-Hot Encoding işlemine tabi tutalım
encoder = OneHotEncoder()
transformed_data = encoder.fit_transform(data[['renk']]).toarray()

# One-Hot Encoding sonrası oluşan yeni veri setini bir DataFrame'e dönüştürelim ve sütun isimlerini belirleyelim
one_hot_data = pd.DataFrame(transformed_data, columns=['kırmızı', 'mavi', 'sarı', 'yeşil'])

# One-Hot Encoding sonrası oluşan veri setini ekrana yazdıralım
print(one_hot_data)
