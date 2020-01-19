import numpy as np
a = np.array([1,2,3])
print(a)

my_list = [1,2,3]
print(my_list)
arr =np.array(my_list)
print(arr)
my_math = [[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(my_math)
print(arr)

arr = np.arange(0,11)
print(arr)
arr = np.arange(0,11,2)
# print(arr)

print(np.zeros((3,4)))
# print(np.ones((3,4)))

arr = np.linspace(0,5,4)
# print(arr)

eye = np.eye(4)
# print(eye)
#
# print(np.random.rand(5))
#
# print(np.random.rand(5,5))

# standard normal distribution
print(np.random.randn(2))
print(np.random.randn(4,4))
print(np.random.randint(1,100,10))
