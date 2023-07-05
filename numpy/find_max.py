def find_max(arr):
  greatest = arr[0]
  greatest_index = 0
  for i in range(1,len(arr)):
    if arr[i] > greatest:
      greatest = arr[i]
      greatest_index = i
  return greatest, greatest_index

arr  = [3, 7, 2, 9, 4]
greatest, greatest_index = find_max(arr)
print("The greatest number of the series:", greatest)
print("Index of the largest number of the array:", greatest_index)
