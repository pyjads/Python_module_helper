#%%
from sklearn import datasets
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
rnd_state = 42
#%%

# loading sample data
housing = datasets.load_boston()
print(housing.keys())

# features
df = pd.DataFrame(housing['data'], columns=housing['feature_names'])
# target
y = housing['target']

print(df.head())

# numpy array of features
X_rows = df.values
print(X_rows)

#%%
#plot the column-column corelation heatmap

# copy of data
data = df.copy()
data['target'] = y
# heatmap plot for correlation idea
sns.heatmap(data.corr(), square=True, cmap='RdYlGn')
plt.show()

#%%
# Linear Regression on RM column and target
X_train, X_test, y_train,y_test = train_test_split(df['RM'].values.reshape(-1,1), y.reshape(-1,1), test_size=0.3)

reg = LinearRegression()
reg.fit(X_train, y_train)

# y_predict = np.linspace(np.min(df['RM'].values),np.max(df['RM'].values)).reshape(-1,1)
# plotting the fit
prediction = reg.predict(X_test)
plt.scatter(df['RM'], y, color='blue')
plt.plot(X_test, reg.predict(X_test), color='black')
plt.show()


# calculating the mean squared error
print('prediction score: {}'.format(reg.score(X_test, y_test)))
print(np.sqrt(mean_squared_error(y_test, prediction)))


#%%

# working with real beijing csv
b_house = pd.read_csv('E:\Pycharm_Workspace\Data_Science\sklearn_module\housing.csv',encoding="ISO-8859-1")
b_house.drop('url', axis=1, inplace=True)
b_house.dropna(axis=1,inplace=True)
# print(b_house.info())
#%%
# printing the heatmap
sns.heatmap(b_house.corr(), square=True, cmap='RdYlGn')
plt.show()

# choosing x=square and y = total_price
X = b_house['square'].values.reshape(-1,1)
y = b_house['totalPrice'].values.reshape(-1,1)

# cross_validation

reg = LinearRegression()
cv_score = cross_val_score(reg, X, y, cv=5)
print(np.mean(cv_score))
#%%
alpha_space = np.logspace(-8, 0, 50)
def display_plot(cv_scores, cv_scores_std):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    print(cv_scores)
    ax.plot(alpha_space, cv_scores)

    std_error = cv_scores_std / np.sqrt(10)
    ax.fill_between(alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2)
    ax.set_ylabel('CV Score +/- Std Error')
    ax.set_xlabel('Alpha')
    ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
    ax.set_xlim([alpha_space[0], alpha_space[-1]])
    ax.set_xscale('log')
    plt.show()


#%%

# working with Ridge Classifier -- which provides the regularization if features are multi-dimensional

#cleaning the data
b_house_clean = b_house.drop(['id','Lng','Lat','Cid','tradeTime','price','district','floor'],axis=1)

#converting all the columns of dataframe to the numeric datatype
b_house_clean = b_house_clean.apply(pd.to_numeric, errors='coerce')
b_house_clean.dropna(inplace=True)
# print(b_house_clean.info())


# feature, target
X = b_house_clean.drop('totalPrice', axis=1).values
y = b_house_clean['totalPrice'].values.reshape(-1,1)
names = b_house_clean.drop('totalPrice', axis=1).columns


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# alpha has to be selected which can be efficiently choosen by the hyper parameter tuning
ridge = Ridge(alpha=0.1, normalize=True)
ridge.fit(X_train, y_train)
prediction = ridge.predict(X_test)

# coefficients plot
ridge_coeff = ridge.coef_
plt.plot(range(len(names)), ridge_coeff[0])
plt.xticks(range(len(names)), names, rotation=60)
plt.ylabel('Coefficients')
plt.title('Ridge')
plt.show()

print(ridge.score(X_test, y_test))
print(np.sqrt(mean_squared_error(prediction, y_test)))

#%%

# One can perform lasso regression whose implementation is similar to the Ridge Regression

#converting all the columns of dataframe to the numeric datatype
b_house_clean = b_house_clean.apply(pd.to_numeric, errors='coerce')
b_house_clean.dropna(inplace=True)
# print(b_house_clean.info())

# feature, target
X = b_house_clean.drop('totalPrice', axis=1).values
y = b_house_clean['totalPrice'].values.reshape(-1,1)
names = b_house_clean.drop('totalPrice', axis=1).columns
print(X.shape)
print(y.shape)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# alpha has to be selected which can be efficiently choosen by the hyper parameter tuning
lasso = Lasso(alpha=0.0000001, normalize=True)
lasso.fit(X_train, y_train)
# coefficients
lasso_coeff = lasso.coef_

# plotting the lasso coefficients
plt.plot(range(len(names)), lasso_coeff)
plt.xticks(range(len(names)), names, rotation=60)
plt.ylabel('Coefficients')
plt.show()

# lasso.fit(X_train, y_train)
prediction = lasso.predict(X_test)

print(ridge.score(X_test, y_test))
print(np.sqrt(mean_squared_error(prediction, y_test)))

#%%

# performing test for various alpha

b_house_clean = b_house_clean.apply(pd.to_numeric, errors='coerce')
b_house_clean.dropna(inplace=True)
# print(b_house_clean.info())

# feature, target
X = b_house_clean.drop('totalPrice', axis=1).values
y = b_house_clean['totalPrice'].values.reshape(-1,1)
names = b_house_clean.drop('totalPrice', axis=1).columns

# you can check both lasso and ridge change Ridge to Lasso or Lasso to Ridge
lasso = Lasso(normalize=True)
lasso_score = []
lasso_score_std = []
for alpha in alpha_space:

    lasso.alpha = alpha

    lasso_cv_score = cross_val_score(lasso, X, y, cv=10, scoring='neg_mean_squared_error')
    lasso_score.append(np.mean(lasso_cv_score))
    lasso_score_std.append(np.std(lasso_cv_score))

display_plot(lasso_score, lasso_score_std)
#%%


# implementation of Multiple Linear Regression using stats api and sl < 0.05 attribute
b_house_clean = b_house_clean.apply(pd.to_numeric, errors='coerce')
b_house_clean.dropna(inplace=True)
# print(b_house_clean.info())

# feature, target
X = b_house_clean.drop('totalPrice', axis=1).values
y = b_house_clean['totalPrice'].values.reshape(-1,1)

# appending 1 for the constant
X = np.append(arr=np.ones((X_train.shape[0],1)).astype(int),values=X_train, axis=1)
y = y_train

import statsmodels.api as sm
X_opt = X[:,[0,1,2,4,5,6,7,8,9]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
print(regressor_OLS.summary())

X_t = np.append(arr=np.ones((X_test.shape[0],1)).astype(int),values=X_test, axis=1)
X_t = X_t[:,[0,1,2,4,5,6,7,8,9]]

prediction = regressor_OLS.predict(X_t)
print(np.sqrt(mean_squared_error(prediction, y_test)))



#%%

# Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
# implementation of Multiple Linear Regression using stats api and sl < 0.05 attribute
b_house_clean = b_house_clean.apply(pd.to_numeric, errors='coerce')
b_house_clean.dropna(inplace=True)
# print(b_house_clean.info())

X = b_house_clean.drop('totalPrice', axis=1).values
# X = b_house_clean['square'].values.reshape(-1,1)
y = b_house_clean['totalPrice'].values.reshape(-1,1)
names = b_house_clean.drop('totalPrice', axis=1).columns


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X_train)
poly_reg.fit(X_poly, y_train)

lin_reg = LinearRegression()
lin_reg.fit(X_poly, y_train)


prediction = lin_reg.predict(poly_reg.fit_transform(X_test))
print(np.sqrt(mean_squared_error(prediction, y_test)))






