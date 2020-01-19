import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(data=randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])
print(df)
# where each column is a pandas series

print(df['W'])
print(type(df['W']))
print(df.W)  # always use column name in bracket
print(df[['W', 'Z']])

df['new'] = df['W'] + df['Y']
print(df)
print(df.drop('new', axis=1, inplace=True))  # axis = 0 means index, and axis =1 means columns
print(df)
df.drop('E', axis=0, inplace=True)
print(df)
print(df.shape)

# ROWS
print(df.loc['A'])  # label based index
print(df.iloc[2])  # number based index
print(df.loc['B', 'Y'])
print(df.loc[['A', 'B'], ['W', 'Y']])
