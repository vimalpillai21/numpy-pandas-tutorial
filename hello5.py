# # def times2(var):
# #     return var*2
# # print(times2(5))
#
# # map() function
#
# seq = [1, 2, 3, 4, 5]
#
#
# # h = list(map(times2,seq))
# # print(h)
#
# def times2(var): return var * 2
#
#
# t = lambda var: var * 2
# print(t(2))
# s = list(map(lambda num: num * 3, seq))
# print(s)
#
# filtered_list = list(filter(lambda num: num % 2 == 0, seq))
# print(filtered_list)
#
# s = 'Hello my name is Vimal Pillai'
# print(s.lower())
# print(s.upper())
# print(s.split())
# tweet = 'Go Sports! #Sports'
# print(tweet.split('#'))
# print(tweet.split('#')[1])
# d = {'k1':1,'k2':2}
# print(d.keys())
# print(d.items())
# print(d.values())
# lst = [1,2,3]
# print(lst.pop())
# print(lst)
# lst = [1,2,3,4,5]
# item = lst.pop()
# print(item)
# first = lst.pop(0)
# print(first)
# lst.append('new')
# print(lst)
print('x' in [1,2,3])
print('x' in ['x','y','z'])
x = [(1,2),(3,4),(5,6)]
for item in x:
    print(item)

for a,b in x:
    print(a)
    print(b)

seq = ['soup','dog','salad','cat','great']
res = list(filter(lambda word: word[0] == 's',seq))
print(res)

