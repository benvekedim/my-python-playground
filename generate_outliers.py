import random

# Rastgele 10 tamsayı içeren bir dizi oluşturuyoruz
data = [random.randint(0, 100) for i in range(10)]

# Rastgele bir pozisyonda aykırı bir değer ekliyoruz
outlier_index = random.randint(0, 9)
data[outlier_index] = random.randint(200, 300)

print("Oluşturulan dizi:", data)
