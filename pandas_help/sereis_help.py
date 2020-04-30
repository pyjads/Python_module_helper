#%%
import pandas as pd
import numpy as np
#%%
# craeting a Series and assigning index

weekday = ['Mon','Tue','Wed','Thurs','Fri','Sat','Sun']
prices = pd.Series(np.random.randint(1,1000, size=7), index=weekday)

# getting the index
print(prices.index)
print(prices.index[:2])
print(prices.index[2])

# setting the name to index
prices.index.name = 'Weekday'
print(prices.index.name)
# index entries cannot be modified individually. You can override it all at once as below but it will reset index name
import calendar
weekday = list(calendar.day_name)
prices.index = weekday
# length of index
print(len(prices.index))
#%%

