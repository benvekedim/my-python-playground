import numpy as np

def generate_dict(row,col,key_start,key_finish):
  #dict values
  values = [np.random.randint(i, size=(row,col)) for i in range(key_start,key_finish)]
  #generated dict with random values
  new_dict = dict(zip(range(key_start,key_finish),values))
  return new_dict
