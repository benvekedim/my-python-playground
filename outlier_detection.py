import random

# Rastgele 10 tamsayı içeren bir dizi oluşturuyoruz
data = [random.randint(0, 100) for i in range(10)]

# Rastgele bir pozisyonda aykırı bir değer ekliyoruz
outlier_index = random.randint(0, 9)
data[outlier_index] = random.randint(200, 300)

print("Oluşturulan dizi:", data)

#Oluşturulan dizi: [241, 3, 46, 49, 90, 87, 24, 50, 21, 56]

# Aykırı değerlerin belirlenmesi için bir aralık belirleyelim
lower_range = np.mean(data) - 2 * np.std(data)
upper_range = np.mean(data) + 2 * np.std(data)

# Aykırı değerleri bulalım
outliers = []
for value in data:
    if value < lower_range or value > upper_range:
        outliers.append(value)


print("lower_range: ",lower_range)
print("upper_range: ",upper_range)
print("Aykırı Değerler:", outliers)
