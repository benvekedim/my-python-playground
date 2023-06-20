import time

def my_function(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

# my_function fonksiyonunun çalışma süresini ölç
start_time = time.time()
my_function(1000)
end_time = time.time()

elapsed_time = end_time - start_time

print('my_function fonksiyonunun çalışma süresi:',
      elapsed_time,
      'saniye')
