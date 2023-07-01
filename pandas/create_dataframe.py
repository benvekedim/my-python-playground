import pandas as pd

data = [
    [1, "John", 32],
    [2, "Jane", 28],
    [3, "Bob", 45],
    [4, "Alice", 27]
]

column_names = ["id", "name", "age"]

def create_dataframe(data, column_names):
    df = pd.DataFrame(data, columns=column_names)
    return df

df = create_dataframe(data, column_names)
print(df)
