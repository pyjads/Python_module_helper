#%%
import pandas as pd
import numpy as np
series = pd.Series([1,2,3,4,5,6,7,8,100], index=['A','B','C','D','E','F','G','H','I'], name='Numbers' )

print(series.agg(np.mean))


#%%
data = pd.DataFrame({'value':[1,2,3,4,5,6,7,8,9,10]})

def compute(row):
    if row['value'] > 5:
        return 'greater than 5'
    elif row['value'] == 5:
        return 'equal'
    else:
        return 'small'

def compute1(data):
    if data == 'greater than 5':
        return 'Hola than 5'
    else:
        return data

data['compute'] = data.apply(compute, axis=1)
data.compute= data.compute.transform(compute1)
print(data)

