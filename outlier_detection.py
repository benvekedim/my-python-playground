data = [241, 3, 46, 49, 90, 87, 24, 50, 21, 56]
data

# Aykırı değerlerin belirlenmesi için bir aralık belirleyelim
lower_range = np.mean(data) - 2 * np.std(data)
upper_range = np.mean(data) + 2 * np.std(data)

# Aykırı değerleri bulalım
outliers = []
condition = ~((lower_range <= data) & (data<=upper_range))
result = np.where(condition)[0][0]
data[result]


print("lower_range: ",lower_range)
print("upper_range: ",upper_range)
print("Aykırı Değerler:", outliers)
