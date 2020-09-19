#%%
from sklearn import datasets
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.style.use('ggplot')
#%%
# load iris dataset
iris = datasets.load_iris()
print(type(iris)) # it is bunch which is just like dictionary

print(iris.keys())
# print(data['feature_names'])
print(type(iris['data']))
print(iris['data'].shape)
print(iris['target'])
#%%
# sns.pairplot
def species(row):
    if row['target'] == 0:
        return 'setosa'
    if row['target'] == 1:
        return iris['target_names'][1]
    if row['target'] == 2:
        return iris['target_names'][2]
sns.set(style="ticks", color_codes=True)
# create dataframe of sklearn datasets
df_iris = pd.DataFrame(iris['data'], columns=iris['feature_names'])
Y = iris['target']
df_iris['target'] = Y
df_iris['flower'] = df_iris.apply(species, axis=1)

sns.pairplot(df_iris, hue='flower')
plt.show()


# performing the countplot
plt.figure()
sns.countplot(x='target', hue='flower', data=df_iris)
plt.show()

#%%

# eda analysis
df_iris = pd.DataFrame(iris['data'], columns=iris['feature_names'])
Y = iris['target']
df_iris['target'] = Y
df_iris['flower'] = df_iris.apply(species)
# plotting scatter matrix
_ = pd.plotting.scatter_matrix(df_iris, c=Y, marker='D', s = 150)
plt.show()

#%%
# knn implementation
from sklearn.neighbors import KNeighborsClassifier
df_iris = pd.DataFrame(iris['data'], columns=iris['feature_names'])
df_target = iris['target']

knn = KNeighborsClassifier(n_neighbors=8)


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(df_iris.values, df_target, test_size=0.2, stratify=df_target)


knn.fit(x_train, y_train)


print(knn.score(x_test, y_test))

# plotting accuracy for training and testing data for iris_data_set
test_acc = [0] * 70
train_acc = [0] * 70
number_neighbors = list(range(1,71))
for i, k in enumerate(number_neighbors):
    k_class = KNeighborsClassifier(k)
    k_class.fit(x_train, y_train)

    train_acc[i] = k_class.score(x_train, y_train)
    test_acc[i] = k_class.score(x_test, y_test)

plt.plot(number_neighbors, train_acc, label='Train')

plt.plot(number_neighbors, test_acc, label = 'Test')
plt.legend()
plt.show()

