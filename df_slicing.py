import pandas as pd

# Örnek bir DataFrame oluşturalım
df = pd.DataFrame({
    'isim': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Ali'],
    'yaş': [25, 28, 31, 27, 24],
    'cinsiyet': ['Erkek', 'Erkek', 'Kadın', 'Kadın', 'Erkek'],
    'maaş': [3000, 3500, 4000, 3800, 3200]
})

# DataFrame'in tamamını yazdıralım
print(df)

# İlk 3 satırı yazdıralım
print(df[:3])

# 2. ve 4. satırları yazdıralım
print(df.iloc[[1,3]])

# 'isim' ve 'maaş' sütunlarını yazdıralım
print(df[['isim', 'maaş']])

# 'yaş' sütununda 30'dan büyük olanların DataFrame'ini yazdıralım
print(df[df['yaş'] > 30])
