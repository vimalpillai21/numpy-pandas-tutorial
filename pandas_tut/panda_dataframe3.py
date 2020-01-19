import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(list(zip(outside,inside)))
print(hier_index)

df = pd.DataFrame(np.random.randn(6,2),hier_index,['A','B'])
print(df)

print(df.loc['G1'].loc[1])
print(df.index.names)
df.index.names = ['Groups','Num']
print(df)

print(df.loc['G2'].loc[2]['B'])

print(df.xs(1,level='Num')) # for level G1 and G2's subsection row 1

