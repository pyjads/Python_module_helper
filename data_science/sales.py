
#%%
import pandas as pd
import numpy as np

def func(row):
    return len(row)

sales = pd.read_csv('data_science/sales_data_sample.csv', encoding='cp1252')
sales.set_index('ORDERDATE', inplace=True)
sales.index = pd.to_datetime(sales.index)
print(sales.index.dtype)
sales['city length'] = sales['CITY'].apply(func)
sales.sort_index(inplace=True)

data = sales['QUANTITYORDERED'].resample('D').min()

sales[['ORDERNUMBER','PRICEEACH']] = sales[['ORDERNUMBER', 'PRICEEACH']].apply(lambda n: n//12)

def greater(row):
    return row > 4

sales['Price > 4'] = sales['PRICEEACH'].apply(greater).map({True:'Yes',False: 'No'})
#%%
import matplotlib.pyplot as plt
df = sales.sort_index()

df = df[['PRICEEACH','ORDERNUMBER','SALES']].pct_change()*100

#%%

df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'), index=['A','B'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))

#%%
austin_dict = {'date':['2016-01-01','2016-02-08', '2016-01-17'],
               'ratings':['Cloudy','Cloudy','Sunny']}

houston_dict = {'date':['2016-01-01','2016-02-08', '2016-01-17'],
               'ratings':['Sunny','Cloudy','Sunny']}

austin = pd.DataFrame(austin_dict)
houston = pd.DataFrame(houston_dict)
austin['date'] = pd.to_datetime(austin['date'])
houston['date'] = pd.to_datetime(houston['date'])
merged = pd.merge_ordered(austin, houston)

#%%
 
s1 = pd.Series(['a', 'b','e'])
s2 = pd.Series(['c', 'd'])

print(pd.concat([s1, s2], keys=['s1','s2']))

#%%
df = pd.DataFrame({'angles': [0, 3, 4],'degrees': [360, 180, 360]}, index=['circle', 'triangle', 'rectangle'])
print(df)
print(df.sub(pd.Series([1, 1, 1], index=['circle', 'triangl', 'rectangle']), axis='index'))

#%%
indexes = pd.Series(['Jan','Jan','Mar','Mar','May','May','July','July','Sep','Sep','Nov','Nov'], index=[1,2,3,4,5,6,7,8,9,10,11,12])
date_sample = sales.groupby(sales.index.month).sum().groupby(indexes).sum()
date_sample2=sales.groupby(sales.index.month).sum()

