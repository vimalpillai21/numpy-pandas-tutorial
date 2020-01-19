import numpy as np

arr = np.arange(25)
print(arr)
randarr = np.random.randint(0,50,10)
print(randarr)
reshaped_arr = arr.reshape(5,5)
# print(reshaped_arr)

print(randarr.max())
print(randarr.min())
print(randarr.argmin())
print(randarr.argmax())
print(arr.shape)
arr = arr.reshape(5,5)
print(arr.shape)
print(arr.dtype)