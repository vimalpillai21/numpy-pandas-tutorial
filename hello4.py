# seq = [1,2,3,4,5]
# for num in seq:
#     print(num)
#     print('Hello')
#     print()

# i=1
# while i < 5:
#     print("i is {}".format(i))
#     i=i+1

# for x in range(0, 5):
#     print(x)
#
# x=[1,2,3,4]
# list(range(0,10))
# out = []
# for num in x:
#     out.append(num**2)
# print(out)
#
# print([num ** 2 for num in x])

def my_func(name="Default name"):
    print('Hello '+name)


my_func("Vimal")
my_func(name="vimal")

def square(num):
    """
    This is a docstring
    can go multiple lines.
    this function squares a number.
    """
    return num ** 2

output = square(23)
print(output)


