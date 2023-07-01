#installing names library
!pip install names

import names

def generate_names(num_names):
    name_list = list(map(lambda x: names.get_first_name(), range(num_names)))
    return name_list

num_names = 5
name_list = generate_names(num_names)
print(name_list)
