#%%

import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

#%%

# create a timestamp using datetime
time_stamp = pd.Timestamp(datetime(2017,1,1)) # automatically set to midnight

# create timestamp without datetime -- u have to use string
print(pd.Timestamp('2-17-01-01')) # here year is incorrect it will not give error but timestamp would be incorrect
assert pd.Timestamp('2017-01-01') == time_stamp


# you can use time_stamp.year , time_stamp.weekday_name
#%%

# building period and frequency

# for period
period = pd.Period('2017-01')
print(period) # default: Frequency set to None

# change freq to daily
period.asfreq('D')
print(period)

# convert it to timestamp and back
period = period.to_timestamp().to_period('M')
print(period)

#%%
# adding days or month to period
period = pd.Period('2017-01')
period = period.asfreq('D') # when you change it to daily from month it will set to last date
print(period)
print(period + 2)

period = period.asfreq('M')
print(period + 2)

# addition and substraction is no longer supported
# print(pd.Timestamp('2017-01-01','D') + 2)

#%%

# date_range usage:
# pd.date_range: start, end, periods, freq

index = pd.date_range(start='2017-01-01', periods=12, freq='D') # freq can be M, H, Y, D etc
print(index) # type is DateTimeIndex

# change index to period
period = index.to_period()
print(period) # type is PeriodIndex

# create a timeseries

df = pd.DataFrame({'data': index})
print(df)

data = np.random.random(size=(12,2))
df1 = pd.DataFrame(data = data, index=index)
print(df1)

#%%

# Indexing and resampling time-series

data = pd.read_csv('time_series/google.csv')

# convert to date
data.Date = pd.to_datetime(data.Date)
data.set_index('Date', inplace=True)

data['Open'].plot()
plt.show()

# indexing for date info
print(data['2013': '2014']) # including 2013 and 2014 year both

# change the frequency of index: for datetimeindex upsampling
data1 = data.asfreq('H')
print(data1.index)

print(data1.isnull().sum())

# plotting subplots
plt.figure(1)
plt.subplot(221)
plt.plot(data.Open, data.index, label = 'OPEN')

plt.subplot(222)
plt.plot(data.High, data.index, label='HIGH')

plt.subplot(223)
plt.plot(data.Low, data.index, label='Low')

plt.subplot(224)
plt.plot(data.Open, data.index, label='Open')
plt.show()

# check datacamp slides for shift, lagged, pct_change, subtract, divide, multiply, chaining operations

#%%

# normalizing the prices, values makes it easier to compare with other data. for this please look at data camp slides
# which they have explained perfectly

# data.div(data.iloc[0]).mul(100) -- Normalizing hint

#%%

# to convert series to dataframe you can use pd.to_frame(<'column_name'>)
# to convert dataframe to series you can use .squeeze()
# learn how to create secondary_y axis
google = pd.read_csv('time_series/google.csv', parse_dates=['Date'], index_col='Date')
google['Close'] = google['Close'].str.replace(',','')
google['Close'] = google.Close.astype('float64')
google.plot(secondary_y=['Close','Open'])
plt.show()

print(google['Open'].rolling('10D').mean()) # try with 10 periods initial 10 rows will be null

# random walk to generate prices similar for a stock
google_close = google['Open']
google_random = np.random.choice(google_close.pct_change(), google_close.count())

google_close_random = pd.Series(google_random, index=google_close.index)

start = google_close.first('D')
google_close_random = start.append(google_close_random.add(1))
print(google_close_random.head())
google_close_random = google_close_random.cumprod()
print(google_close_random.head())

google_close.plot()
google_close_random.plot()
plt.show()


# correlation
print(google.corr())
import seaborn as sns
sns.heatmap(google.corr(), annot=True)
plt.show()

#%%

# rolling
google = pd.read_csv('time_series/google.csv', parse_dates=['Date'], index_col='Date')
google['Close'] = google['Close'].str.replace(',','')
google['Close'] = google.Close.astype('float64')
print(google['Open'].head())
moving_average = google[['Open']].rolling(window='30D').mean().add_suffix('_MA90')
print(moving_average.head())
newdata = google[['Open']].join(moving_average)
# print(newdata.head())
newdata.plot()
plt.show()

#%%

google = pd.read_csv('time_series/google.csv', parse_dates=['Date'], index_col='Date')
google['Close'] = google['Close'].str.replace(',','')
google['Close'] = google.Close.astype('float64')

# normalizing
normalize = google['Open'].div(google['Open'].iloc[0]).mul(100)
normalize.plot()
plt.show()


# running rate
run_rate = google['Open'].pct_change()
run_rate = run_rate.add(1)
run_rate = run_rate.cumprod().sub(1)
run_rate = run_rate*100
run_rate.plot()
plt.title('Running Rate')
plt.show()

# 1000 dollars investment
run_rate = google['Open'].pct_change()
run_rate = run_rate.add(1)
print(run_rate.head())
print()
run_rate = run_rate.cumprod()
print(run_rate.head())
run_rate = run_rate*1000
run_rate.plot()
plt.title('1000 dollar investment')
plt.show()

# yearly return
def year_return(prod_return):
    return np.prod(prod_return +1 ) -1

yearly = google['Open'].pct_change()
yearly = yearly.rolling('360D').apply(year_return)
yearly = yearly*100
yearly.plot()
plt.show()


#%%
# second nan would be taken as
data = pd.DataFrame({'A':[np.nan, 100, 101, 100, 200, np.nan, 100, 200, 101]})
d = data.pct_change()
print(d)
print()
d = d.cumprod().subtract(1).multiply(100)
print(d)
#%%

# joinplot, heatmap
data = pd.DataFrame({'A':[100,200,300,400,500,600], 'B':[1,3,4,5,1,1]})

sns.jointplot(x='A', y='B', data= data)
plt.show()
sns.heatmap(data.corr(), annot=True)
plt.show()

print(data.corr())

#%%

