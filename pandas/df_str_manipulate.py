import pandas as pd

# Örnek bir DataFrame oluşturmak
data = {'isim': ['Ali', 'Mehmet', 'Ayşe', 'Fatma'],
        'soyisim': ['Yılmaz', 'Kaya', 'Demir', 'Kara'],
        'email': ['ali.yilmaz@example.com', 'mehmet.kaya@example.com', 
                  'ayse.demir@example.com', 'fatma.kara@example.com']}
df = pd.DataFrame(data)
print(df)

# 'isim' sütununu büyük harflere dönüştürme
df['isim'] = df['isim'].str.upper()

# 'soyisim' sütununu küçük harflere dönüştürme
df['soyisim'] = df['soyisim'].str.lower()

# 'email' sütunundan sadece domain adlarını almak
df['domain'] = df['email'].str.extract('@(.+)$')

# 'isim' ve 'soyisim' sütunlarını birleştirme
df['tam_isim'] = df['isim'] + ' ' + df['soyisim']

# 'email' sütunundaki dizeyi bir alt dizeye göre bölmek
df[['kullanici_adi', 'domain']] = df['email'].str.split('@', expand=True)

# 'email' sütunundaki belirli bir alt dizeyi içeren satırların seçilmesi
df[df['email'].str.contains('example')]
