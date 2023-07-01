import pandas as pd
import names
import random

length = 50  #df.shape[0]

def num_generate(num):
    return num + 1

ids = list(map(num_generate, range(length)))

def generate_names(length ):
    name_list = list(map(lambda x: names.get_first_name(), range(length )))
    return name_list

name_list = generate_names(length)

def num_arr_generate(length):
    arr = [random.randint(1, 80) for _ in range(length)]
    return arr

age_list = num_arr_generate(length)

data = list(
    map(list,zip(ids,name_list,age_list))
)


column_names = ["id", "name", "age"]

def create_dataframe(data, column_names):
    df = pd.DataFrame(data, columns=column_names)
    return df

df = create_dataframe(data, column_names)
print(df)
