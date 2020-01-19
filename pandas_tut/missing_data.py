import numpy as np
import pandas as pd

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)
print(df.dropna(axis=1)) # axis = 0 for row, axis = 1 for y axis
print(df.dropna())
print(df.dropna(thresh=2)) # row with minimum number of nan values will be dropped
print(df.fillna(value='Fill Value'))
print(df['A'].fillna(value=df['A'].mean())) # filling value of missing in col as mean of col
