import numpy as np

arr = np.arange(0, 11)
# print(arr)
# print(arr[8])
# print(arr[2:6])
# print(type(arr))
# print(arr[:6])  # arr[0:6]
# print(arr[5:])

# print(arr)
# arr[0:5] = 100
# print(arr)
arr = np.arange(0,11)
print(arr)
slice_of_arr = arr[0:6]
print(slice_of_arr)
# broadcasting
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)

arr_copy = arr.copy()
print(arr)
arr_copy[:] =100
print(arr)
print(arr_copy)

