import pandas as pd

# DataFrame Example
data = {'a': [1, 2, 3, 1, 2, 3],
        'b': [4, 5, 4, 5, 4, 5]}

df = pd.DataFrame(data)

# Calculating the number of values by columns
count_a = df['a'].value_counts()
count_b = df['b'].value_counts()

print(count_a)
print(count_b)
