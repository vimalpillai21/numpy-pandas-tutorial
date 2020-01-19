import numpy as np

arr_2d = np.array([[5,0,15],[20,25,30],[35,40,45]])
# print(arr_2d)
# print(arr_2d[0][0])
# print(arr_2d[0])
# print(arr_2d[1][1])
# print(arr_2d[2][1])
# print(arr_2d[2,1])
# print(arr_2d[1][2])
# print(arr_2d[:2,1:])
print(arr_2d[:2])
arr = np.arange(1,11)
print(arr)
print(arr >5)
bool_arr = arr > 5
print(arr[bool_arr])
print(arr[arr>5])

print(arr[arr<3])
arr_2d = np.arange(50).reshape(5,10)
print(arr_2d,end="\n\n")
print(arr_2d[1:3,3:5])
print(arr_2d[1:3])

