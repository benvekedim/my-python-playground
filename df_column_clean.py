# Örnek bir DataFrame oluştur
df = pd.DataFrame({'Product ID': ["a123", "b143", "c234"]})

# Product ID kolonunu temizle ve yeni kolonu oluştur
df['Product ID Cleaned'] = df['Product ID'].str.extract('(\d+)', expand=False).astype(int)

# Yeni DataFrame'i yazdır
print(df)
