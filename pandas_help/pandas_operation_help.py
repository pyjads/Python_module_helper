# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# this module has basic operations
data = pd.read_csv('pandas_help/winter.csv')
dataset = pd.read_csv('pandas_help/wine_data.csv', sep=';')

# if you have na values you can mention in pd.read_csv()
# if suppose in A column of data na_values are mentioned by -1 and in B column of data na_values are mentioned by -2
# in that case we can use below code:
#
# df = pd.read_csv(<dataframe>, na_values={'A':[], 'B':[]})

# %%

# to get the shape
print(data.shape)  # show (rows, columns)

# %%

# to get data type of columns
print(data.dtypes)

# %%

# to get info

print(data.info())
# %%
# to get all the values as a list of list and want to ignore index
print(data.values)

# %%

# to get columns

print(data.columns)

# df.columns = df.columns.str.strip() to remove spaces

# if you want to drop a columns use df.drop([<column name list>, axis='columns'])

# selecting column with all non-zeros values df2.loc[:, df2.all()] --> missing values will be taken as non-zero

# selecting column with any NaN, df.loc[:, df.isnull().any()]

# dropping rows with any Nan df.dropna(how='any) how='all' will remove a row in which all columns are null you can provide
# thresh=<int> to drop rows/columns if it is equal or greater than thresh

# %%

# to get index
print(data.index)

# %%

# to reset index
data = data.reset_index()

# %%

# to get top 5 rows,  you can use to get top n rows using data.head(<num of rows needed>).
print(data.head())

# %%

# to get below 5 rows, you can use to get bottom n rows using data.tail(<num of rows needed>).
print(data.tail())

# %%

# to get frequency count of a column
# value_counts is a function of Series not of dataFrame so cannot be applied as data.value_counts(dropna=False)
unique = data['Year'].value_counts(dropna=False)  # dropna= False will include na values
print(unique)

# %%

# to get statistics use data.describe() only the columns with numeric data type will be return

# %%

# for plotting the histogram
dataset.plot('quality', subplots=True)  # this will apply to all numeric columns and show result
plt.show()

# %%
# dataframe plot

iris = pd.read_csv('pandas_help/iris.data', header=None,
                   names=['petal width', 'petal length', 'sepal width', 'sepal length', 'species'])
iris.plot(x='sepal length', y='petal length')  # here you can provide y as list ['petal length', 'sepal width'] also you
# can provide s=sizes
plt.show()

# %%

# you can plot histogram of single column as
dataset['quality'].plot(kind='hist')  # can pass logx=True or logy = True for logarithmic scale and rot=70 will rotate
# the axis scale by 70 degree. You can also pass cumulative=True in hist for cumulative distribuiton
plt.legend(['Quality'])
plt.show()

# for specifying xlim and ylim use plt.xlim(0,10) or plt.ylim(0,10)
# %%

# boxplot can be used to see outliers
data.boxplot(column='Year', by='Gender')  # rot = 90 will rotate the axis scale by 90 degree
plt.show()

iris = pd.read_csv('pandas_help/iris.data', header=None,
                   names=['petal width', 'petal length', 'sepal width', 'sepal length', 'species'])
iris.plot(y=['petal length', 'sepal length'], kind='box')
plt.show()

iris['petal length'].plot(kind='hist', cumulative=True, density=True)
plt.show()

# %%

# scatter plot can be used to see outliers as well
iris = pd.read_csv('pandas_help/iris.data', header=None,
                   names=['petal width', 'petal length', 'sepal width', 'sepal length', 'species'])
iris.plot(x='sepal length', y='petal length')
plt.show()

iris.hist()  # this will plot all the numeric columns hist as different subplots
plt.show()

# %%

# melting the data use pd.melt(frame=<dataframe> , id_vars=[<to be kept constant>], value_vars=[<columns to melt>],
# var_name=<>, value_name=<>)


# %%

# pivoting data
# pivot cannot handle duplicate values use pivot_table
# data.pivot(index=<used as indexing>, columns=<to pivot>, value=<pivot colummns to fill>)

# %%
# pivot_table
# data.pivot_table(index=<columns used as indexing>, columns=<column to pivot>, values=<pivot columns to fill>, aggfunc=)

d = data.pivot_table(index=['Year', 'Country'], columns=['Gender', 'Medal'], values='Athlete', aggfunc='count')
d['Total'] = d.apply(np.sum, axis=1)  # axis =1 will apply row wise
print(d)

d.reset_index(inplace=True)
print(d.head())

# %%

# if we have a function that takes multiple values and we want to apply that function to dataframe
# then we have specify that in apply()
# like if we have a function  def diff_money(row, pattern)
# then df.apply(diff_money, axis=1, pattern=pattern) axis=1 will work row wise

# %%

# concatenate data in pandas for concatenating use, pandas.concat([<dataframe_list>], ignore_index=True) it will take
# the original dataframe indexes. so you have to reset the index by passing ignore_index=True, this will be row wise
# concatenation. For column wise concatenation pass axis=1 and data are joined based on index value equality

#

# %%

# if two dataframes do not have same order than we can merge the data

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]}, index=['A','B','C','D'])
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]}, index=['C','D','A','F'])

# here if we want to merge df1 and df2 but notice they don't have same order so we cannot concatenate with axis=1
# so we can merge the df1 and df2 using pd.merge during this type of merge  index is ignored

merged = pd.merge(left=df1, right=df2, left_on='lkey', right_on='rkey')
print(merged)

# There are three types of merge one-to-one, manytoOne/onetomany and manytomany

# %%

# converting one type to another
# example: if we want to convert A column of data to str
# data['A'] = data['A].astype(str)
#
# example: if we want to convert A column of data to category --> category datatype is memory efficient
# data['A'] = data['A'].astype('category')


# %%

# suppose you have a numeric column but it has been set to object because of empty fields
# this can be taken care by
# df['A'] pd.to_numeric(df['A'], errors='coerce')
# above errors='coerce' anything that cannot be converted to numeric data type will be NaN
# if we do not pass errors='coerce' will return an error because python will have no idea what to do with string value

s = pd.Series(['apple', '1.0', '2', -3])
s = pd.to_numeric(s, errors='coerce')
print(s)

# %%

# converting a column to datetime use pd.to_datetime() you can provide format='' to format your datetime

# %%

# use reindex(<index list>) usullay used in datetime index
# suppose u have datetime index and you want to reindex using certain dates you use pd.to_datetime() to get
# datetime Series and use data.reindex(<series of datetime>)

s = pd.Series([1, 2, 10000000, 12, 13])
st = data.reindex(s,
                  method='ffill')  # if for example 10000000 is not the index in data so it will fill the row with NAN
# you can provide method='ffill' etc. for filling nan values
print(st)

# %%

# pattern matching
# $17.895 = ^\$\d*\.\d*{2}$
# pattern = re.compile('^\$\d*\.\d*{2}$')
# result = pattern.match('$17.85')
# bool(result) --> return True or False if the pattern has matched


import re

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries220 and 1 banana')

# Print the matches
print(matches)

# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

# Write the second pattern
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

# Write the third pattern
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)

# pattern = '^[A-Za-z .]*$'
# mask = countries.str.contains(pattern)

# %%

# dealing with duplicate data
# use: .drop_duplicates() it will drop the rows not the columns

# %%

# dealing with the missing values
# use: .dropna() it will drop the rows where in any column there is missing value

# to fill missing values
# use: .fillna
# df['A'] = df['A'].fillna('missing') it will overide na values with missing
#
# using with multiple columns
# df[['A','B']] = df[['A','B']].fillna(0) --> it will fill all missing values in 'A' and 'B' with 0
#
# filling missing value with test statistics
# median is a better statistics for outliers
#
# if you want to fill na values of a column with mean:
# mean_value = df['A'].mean()
# df['A'] = df['A'].fillna(mean_value)


import numpy as np

np.random.seed(42)
d = {
    'value1': [1, 2, 3, 4, np.nan, 5, 6],
    'value2': [1, 2, 3, np.nan, 5, 6, 7],
    'value3': [np.nan, 2, 3, 4, 5, 6, 7]
}
df = pd.DataFrame(d)
df['value1'].fillna(df['value1'].mean(), inplace=True)
print(df)

print(df.all())

df.plot(color='red', marker='d', legend=True, subplots=True)  # legend can be set to True
plt.show()


# if you want fillna with row mean
def row_mean(row):
    # here row is of type Series
    m = row.mean()
    row = row.fillna(m)
    return row


df = pd.DataFrame(d)
df = df.apply(row_mean, axis=1)
print(df)

# %%

# asserting if a column has no null value
# assert data.A.notnull().all()

assert data.Year.notnull().all()

# data.notnull() --> return dataframe where each row of each column is set to True or False if it is null or not
# data.notnull().all() --> return series where each column has null values or not
# data.notnull().all().all() -> return single true or false which shows if all the any value in dataframe is null or not
#
# Assert that all values are >= 0
# assert (data >= 0).all().all()
# %%
iris = pd.read_csv('pandas_help/iris.data', header=None,
                   names=['petal width', 'petal length', 'sepal width', 'sepal length', 'species'])

# use of quantile --> value should be between 0 to 1
q = iris.quantile([0.5, 0.75])
print(q)

# count() is used to get the not null values
print(iris.count())

# unique() is used to get unique values present in a column it is a series method not a dataframe method
print(iris['species'].unique())

# %%

# rolling() works similar to accumulate()
# if you want to find mean of last 24 rows use as df.rolling(window=24).mean()

# %%

# you can use str operation on a column like str.contain() str.replace

# if a column is datetime object then you can use .dt.hour or dt.month
# but if index is datetime and you want to excess year data.index.dt.year is wrong.. you can directly use
# as data.index.year

# you can localize dt like .dt.tz_localize('US/Central') then you can covert to other timezone like .dt.tz_convert('US/Eastern')

# %%

# you can use resample on the datetime columns as df['A'].resample('D').first() or sum() or max() or mean() or ffill etc.


# %%

# you can use interpolate('linear') on a series
# %%
# you can use map on a series object like:
# for sales.csv

sales = pd.read_csv('pandas_help/sales_data_sample.csv', encoding='cp1252')
sales.set_index('ORDERDATE', inplace=True)
sales.index = pd.to_datetime(sales.index)


def greater(row):
    return row > 4


sales['Price > 4'] = sales['PRICEEACH'].apply(greater).map({True: 'Yes', False: 'No'})

# %%

# dataframe supports multiple indexes you can use .set_index() and pass the list to be set as index
# for multi level index use .index.names

# do not forget to use .sort_index()


data = pd.read_csv('pandas_help/winter.csv')
data['Year'] = data['Year'].astype('int64')
# setting multiindex of Year and Country
data.set_index(['Year', 'Country'], inplace=True)
data.sort_index(inplace=True)
print(data.index.names)

# for accessing using multi index you have to use the concept of tuple
print(data.loc[(1924, 'AUT')])  # get all columns of year 1924 and country 'AUT'

# if you want to slice only with the outer index
print(data.loc[1924])  # return all the rows of year 1924 the whole country index of yeaar 1924 will be included
print(data.loc[1924:1932])

# fancy indexing
print(data.loc[([1924, 1932], 'AUT'), :])  # you have to put : in columns else it will give error
print(data.loc[([1924, 1932], ['AUT', 'CAN']), :])  # you have to put : in columns else it will give error
print(data.loc[(slice(None), ['AUT', 'CAN']), :])  # ignore the outer index and include inner index
print(data.loc[(1924, ['AUT', 'CAN']), :])
print(data.loc[(slice(None), slice('AUT', 'BEL')), :])  # slice on inner index is like 'AUT':'BEL'

# %%

# for multi level index if you want to remove an index and add it to column you can use unstack(level=<index>)

data = pd.read_csv('pandas_help/winter.csv')
data['Year'] = data['Year'].astype('int64')
# pivotting of Year and Medal
data = data.pivot_table(index=['Year', 'Medal'], columns='Gender', values='Athlete', aggfunc='count')
data.sort_index(inplace=True)

# if I want to unstack Country the index is 0 so
data = data.unstack(level='Medal')
print(data.head())

# we can stack using data.stack(level='gender')
data = data.stack(level='Medal')
print(data)

# you can also swap the indexes using data.swapleve(index1, index2)
data = data.swaplevel(0, 1).sort_index()
print(data.head())

# %%
data = pd.read_csv('pandas_help/winter.csv')
data['Year'] = data['Year'].astype('int64')

# %%
# groupby
# you can groupby another series provided both (Series, and DataFrame) should have same index

# you can perform multiple aggregation using groupby by using .agg([<list of agg>])
# for example .agg(['max','mean'])
# you can also provide custom aggregation
# .agg also accepts dictionary input for operation like:
# .agg({'Medal':'count','Athlete':np.concat}) # this will perform count operation on Medal column and concat operation
# on Athlete column


data = pd.read_csv('pandas_help/winter.csv')
data['Year'] = data['Year'].astype('int64')

group = data.groupby('Medal').count()
print(group)

# suppose your dataframe index is datetimeindex and you want to groupby weekday you can do as below

sales = pd.read_csv('pandas_help/sales_data_sample.csv', encoding='cp1252')
sales.set_index('ORDERDATE', inplace=True)
sales.index = pd.to_datetime(sales.index)
by_day = sales.groupby([sales.index.year, sales.index.strftime('%a')])# here we grouping by year then by day
# if you want to see the group use .groups

# if you want to iterate
# for group_name, group in splitting:

unit_sum = by_day['quantityOrdered'.upper()].sum()
print(unit_sum)


# suppose you are grouping the data and you want to use .apply() custom function that custom function return type can
# be a dataframe

# TODO: The result should be 5 columns only but the output row is way longer. records are duplicated

def group_by_status(group):
    print('called')
    df = pd.DataFrame(
        {
            'Status': group['STATUS'],
            'Quantity': group['QUANTITYORDERED'].sum()
        }
    )
    return df


sales = pd.read_csv('pandas_help/sales_data_sample.csv', encoding='cp1252')
sales_data = sales.groupby('STATUS').apply(group_by_status)
print(sales_data.head())


# classic way of using groupby
'''
by_sex_class = titanic.groupby(['sex','pclass'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())

# Impute age and assign to titanic['age']
titanic.age = by_sex_class['age'].transform(impute_median) # transform can be replaced with apply as well here
'''

# group object comprehension example
'''
chevy_means = {year: group.loc[group['name'].str.contains('chevrolet'), 'mpg'].mean() 
                for year, group in splitting}
pd.Series(chevy_means)
'''

# boolean groupby
'''
chevy = auto['name'].str.contains('chevrolet')
auto.groupby(['yr', chevy])['mpg'].mean()
'''

# you can use .filter in a groupby
'''
by_com_sum = by_company['Units'].sum()
print(by_com_sum)

# Filter 'Units' where the sum is > 35: by_com_filt
by_com_filt = by_company.filter(lambda g: g['Units'].sum() > 35)
'''

# you can use map in a groupby
'''
# Create the Boolean Series: under10
under10 = (titanic['age'] < 10).map({True:'under 10', False:'over 10'})

# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)
'''
# %%
# TODO: some extra stuff to be looked upon
# .transform() is used to transform the column look into pandas glossary
sales = pd.read_csv('pandas_help/sales_data_sample.csv', encoding='cp1252')
# sales.set_index('ORDERDATE', inplace=True)
# sales.index = pd.to_datetime(sales.index)

def filling(series):
    series = 120
    return series

sales['QUANTITYORDERED'] = sales[sales['QUANTITYORDERED']>24]['QUANTITYORDERED'].apply(filling)

#%%
# you can use .divide() method as df1.divide(series1, axis='rows')
# you need this because df1/series2 will not work usually because column labels are not equal

d = {
    'value1': [1, 2, 3, 4, np.nan, 5, 6],
    'value2': [1, 2, 3, np.nan, 5, 6, 7],
    'value3': [np.nan, 2, 3, 4, 5, 6, 7]
}

series = pd.Series([100,2,3,4,5,6,7])
df2 = pd.DataFrame({
    'value1':[1,2,3,4,5,6,7],
    'value2':[7,6,5,4,3,2,1]
} ) # try with , index=['A','B','C','D','E','F','G']

df1 = pd.DataFrame(d)

# below code will not work
# in order for this to work df2 should have same column label as df1
print(df1/df2)

# instead use .divide() where argument of divide should be series in series division indexing will not taken
# into consideration

# .divide() with argument of divide as dataframe will only work if both have same columns labels
print(df1.divide(df2, axis='rows'))

# pct_change() is use for currentvalue - previous value

print(df2.pct_change())

# if you add two data frames
print(df1 + df2) # column label of df1 should be same as column label in df2 to be added else it will result in nan
# above df2 mention column label as value4 and value5, and then replace with value1 and value2

# if in df2 column labels are value1 and value2 and you add it will df1 value1 and value2 columns with nan will output
# to nan but if in that case you can add .add() with argument fill_value=0 where nan value will be replaced by 0
print(df1.add(df2, fill_value=0)) # you can chain it with .add() again

# also .add can be used with series as well but fill value will not be valid
print(df1.add(series, axis='rows')) # in this case index column of df1 will not be taken into consideration

# similar to add we have multiply


