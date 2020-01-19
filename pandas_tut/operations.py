import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']
                   })
print(df.head())
print(df['col2'].unique())
print(len(df['col2'].unique()))  # returns unique values as list
print(df['col2'].nunique())  # returns count of unique values
print(df['col2'].value_counts())  # returns unique value counts and no of times
print(df[(df['col1']>2) & (df['col2'] == 444)])
print(df['col1']>2)

def times2(x):
    return x*2

print(df['col1'].apply(times2)) # applying custom function to panda columns
print(df['col3'].apply(len))
print(df['col2'].apply(lambda x: x*2))
print(df)
print(df.drop('col1',axis=1)) # inspace = True
print(df.columns)
print(df.index)
print(df.sort_values('col2'))
print(df.sort_values(by='col2')) # same as above
print(df.isnull())

data = {
    'A':['foo','foo','foo']
}