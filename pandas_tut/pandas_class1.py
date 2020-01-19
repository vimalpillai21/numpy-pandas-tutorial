# pandas Series practice
import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

ser1 = pd.Series(data=my_data)
print(ser1)

ser2 = pd.Series(data=my_data,index=labels)
print(ser2)

ser3 = pd.Series(data=arr,index=labels)
print(ser3)

print(pd.Series(d))
print(pd.Series(data=labels))
print(pd.Series(data=[sum,print,len]))

ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
print(ser1)
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
print(ser2)
print(ser1['USA'])
ser3 = pd.Series(data=labels)
print(ser3)
print(ser3[0])
ser4 =ser1+ser2
print(ser4)