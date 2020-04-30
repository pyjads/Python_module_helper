import pandas as pd
import numpy as np
d = {
    'name': ['sanket','sanchita','medhavi','rohan','sanket','sanchita','medhavi','rohan'],
    'rating': ['tmax','tmax','tmax','tmax','tmin','tmin','tmin','tmin'],
    'val' : [14,8,7,6,1,2,13,4],
    'imdb': [10,2,3,4,5,6,7,10],
    'sex': ['m','f','f','m','m','f','f','m'],
    'color':['red','yellow','green','orange','red','yellow','green','orange']
}
#%%
df = pd.DataFrame(d,index=['A','B','C','D','E','F','G','H'])
# df['sex'] = df.apply(lambda x: x['sex'].upper(), axis=1)
# s = df['value'].sum()
# df['total'] = s
# df['diff']= df.apply(lambda x: x['total']-x['value'], axis=1)

def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.fillna(0)
    numeric = pd.to_numeric(no_na, errors='coerce')
    # print(numeric)
    ge0 = numeric >= 0
    return ge0


# print(df[['value']].apply(check_null_or_valid, axis=1).all().all())

# df['value'] = df['value'].astype('object')
# print(df.info())
#
# df['value'] = pd.to_numeric(df['value'], errors='coerce' )
# print(df.info())

# print(df['name'].str)
selection = (df['imdb'] > 5).map({True:'good_movie',False: 'bad movie'})
group = df.groupby(selection)['imdb'].count()

#%%

mf_group = df.groupby(['sex'])
key = mf_group.groups.keys()
s = mf_group.mean()
#%%

# df['imdb'] = df['imdb'].fillna(df['imdb'].mean())
# df['val'] = pd.to_numeric(df['val'])
df['summation'] = df.apply(lambda x: x['val']+x['imdb'], axis=1)
td = np.log10(df)

#%%

city = ['Indore', 'Bhopal', 'Jaipur', 'Chennai']
literacy = [78, 63, 89, 54]
gdp = [45, 18, 34, 4]
sex_ratio = [79, 45, 78, 95]

col_labels = ['city','literacy', 'gdp', 'sex_ratio']
data = [city, literacy, gdp, sex_ratio]

city_data = list(zip(col_labels, data))
print(city_data)

city_frame = pd.DataFrame(dict(city_data))

#%%

csv = pd.read_csv('./data_science/sanket.csv', )
csv.index = csv['name']
#%%

iris = pd.read_csv('./data_science/iris.data',header = None,names=['petal width','petal length','sepal width','sepal length','species'])
print(iris[['petal width','petal length', 'sepal width']].transform([np.sqrt, np.exp], axis='columns'))
# iris.index = iris['species']
iris.set_index(['species'], inplace=True)
iris.reset_index(inplace = True, drop=False)

#%%
import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('./data_science/iris.data',header = None,names=['petal width','petal length','sepal width','sepal length','species'], index_col='species')

print(iris.groupby('species').mean())


# fig, ax = plt.subplots(figsize=(8,6))
# for label, data in dataset:
#     plt.plot(x='petal width',y='petal length', label=label,kind='scatter')
# dataset.plot(kind='scatter',x='petal width', y = 'petal length', ax=ax)
# plt.legend()
plt.show()
#%%
print(help(plt.legend))

#%%
roll_data = {'roll':[1,2,3,4,5,6,7,8,9]}
roll = pd.DataFrame(roll_data)

roll_rolling = roll.rolling(window=2).mean()
print(roll_rolling)
#%%
# df['imdb'] = df['imdb'].fillna(0)
t = df['val'] > 4
print(t)
print(t.mean())

#%%
serie = pd.Series([1,np.nan,7,np.nan,5,6,np.nan,8], name='values',index=['a','b','c','d','e','f','g','h'])
serie = serie.interpolate('linear')
# print(serie[serie>5])
#%%

print(df['val'].rolling(2).sum())

#%%
import pandas as pd
import numpy as np
mdict = {'Treatment':['A','B','A','C','A','B'],
          'gender':['L','F','M','M','F','M'],
          'id':[1,1,8,2,3,9],
         'system':[10,20,30,40,50,60]
          }
medical = pd.DataFrame(mdict)
m =medical.set_index(['Treatment','gender']).sort_index()
print(m)
# p = medical.pivot_table(index='gender', columns='id', aggfunc={'Treatment': lambda x: ','.join(x)})
# print(p)
index = [5,4,3,2,1,0]
diesease = pd.Series(['malaria','cholera','tb','cancer','hiv','fever'], index=index)

medical['diesease'] = diesease

print(m.groupby('Treatment').count())

#%%

g = medical.groupby(['gender','Treatment'])
medical['mean'] = g['id'].transform(np.sum)
#%%
print(m)

grup_m = m.groupby(['gender'])
elos = grup_m.transform(np.sum)
print(elos)
#%%
import pandas as pd
import numpy as np
import math
print('--------------------------------------')
def grup_sum(group):

    print(group)
    return group.sum()


fb = pd.read_csv('./data_science/sanket.csv', header=0)
g_fb = fb.groupby('A')[['C','D']].apply(grup_sum)
print(g_fb.index)
print(fb.groupby('A').sum())
#%%
series = pd.Series([1,1,1,4,5,6])
print(series.nunique())
#%%
fb = pd.read_csv('./data_science/sanket.csv', header=0)

def print_fb(x):
    print(x)

a = fb['C'].map(lambda x: 'I am a {}'.format(x) )

#%%
import numpy as np
import pandas as pd



medals = pd.read_csv('./data_science/winter.csv')

medal_list = medals.pivot_table(index=['Country','Medal'], columns='Gender',values='Athlete', aggfunc='count')
medal_list = medal_list.unstack(level='Medal')
print(medal_list)

#%%
import numpy as np
import pandas as pd
import os
os.chdir(r'E:\Pycharm_Workspace\Data_Science\data_science')


medals = pd.read_csv('winter.csv')

tab = pd.crosstab([medals['Country'], medals['Gender']], [medals['Medal'],medals['Year']], values=medals['Athlete'], aggfunc='count')
tab['total'] = tab.apply(np.sum, axis='columns')
print(tab)

# medal_list = medals.groupby(['Country','Gender','Medal'])['Medal'].count()
# medal_list = medal_list.unstack(level=['Gender','Medal'])
# print(medal_list)
#%%
import pandas as pd

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'lkey': ['foo', 'bar', 'bar', 'foo'],
                    'value': [5, 6, 7, 8]})

df3 = df1.merge(df2, left_on='lkey',right_on='lkey', how='outer')

#%%
import matplotlib.pyplot as plt
l = [ i for i in range(50)]
k = [i**2 for i in range(50)]

plt.subplot(2,2,1)
plt.plot(l,k, color='red')
plt.subplot(2,2,2)
plt.plot(l,k,color='green')
plt.subplot(2,2,3)
plt.plot(l,k, color='blue')
plt.show()