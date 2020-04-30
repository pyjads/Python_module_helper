#%%
# visit https://www.youtube.com/watch?v=ZB7BZMhfPgk for numpy axis explanation: around 1hr 42min
import numpy as np


# create a pseudo number generator
# but if you seed it and use it on different random functions then result will be different
np.random.seed(42)
#%%
# 1D array
a = np.array([1,2,3,4,5], dtype='float')

print(a)
print(a.ndim)

# 2D array sample
# changing the elements
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
a[1][2] = 100
# print(a)

a[:,2] =200
print(a)

# use np.nditer() for iterating through all the values irrespective of the of the shape
for i in np.nditer(a):
    print(i)

#%%
# 2D array
b = np.array([[1,2,3,4,5],[11,12,13,14,15],[16,17,18,19,20]], dtype='int32')

print(b.shape)
print(b.ndim)
print(b.size)
print(b.itemsize)
print(b.nbytes)

#%%
# numpy array of size 3,4,5 where 3 is number of arrays inside one big array and in each array there are 4 rows
# 5 columns
c = np.random.rand(3,4,5)
print(c)
print(c.shape)
print(c.ndim)
print(c.size)
print(c.itemsize)
print(c.nbytes)

# accessing elements
print(c[0,0])

# accessing with the stepsize --> startIndex:endIndex:stepsize
print(c[0,0,0::2])

# changing the elements
c[:,0] = [5,3,5,1,2]


# changing the elements
c[:,:,1] = 10
# print(c)

# changing the elements
c[: , 1] = [12,13,14,15,16]
print(c)

#%%

# Initializing different types of Array

# creating 0 numpy array of certain dimension
z = np.zeros((2,3))
print('\nZeros Array Of {} size'.format(z.shape))
print(z)

# using empty_like
t = np.random.rand(2,3)
z1 = np.empty_like(t)
print(t)
print('\nCreating similar array of size similar to t')
print(z1)

# creating empty array
z1 = np.empty((2,3))
print('\nCreating empty array')
print(z1)

# creating array of 1's also you can use one_like for similar array of 1 of any other array
z1 = np.ones((3,4,2))
print('\nArrays of all one\'s of shape {}'.format(z1.shape))
print(z1)

# if you want to create an array of certain value use np.full
value = 66
z1 = np.full((3,4,1),value)
print('\n Array of shape {} where each element is of value {}'.format(z1.shape, value))
print(z1)

# if you want to craete an array of certain value of any other given array size
t = np.random.rand(2,3)
value = 12
z1 = np.full_like(t, value)
print('\n Array of shape {} which is similar to t with all the values {}'.format(t.shape, value))
print(z1)

# create an array of given size with uniform distribution for normal distribution use randn
z1 = np.random.rand(3,4,4)
print('\n Random array of shape {} with all decimal numbers between 0 to 1'.format(z1.shape))
print(z1)

# generate an array of number between certain value only integers
low = 1
high = 100
z1 = np.random.randint(low, high, size=(3,4))
print('\n Random Array between {} and {} of shape {}'.format(low,high, z1.shape))
print(z1)

# generate an array of number between certain values where float is also allowed uniform distribution
# can be use
low = 1
high = 100
z1 = np.random.uniform(low, high, size= (3,4))
print('\n Random Array following Uniform distribution between {} and {} of shape {}'.format(low, high, z1.shape))
print(z1)

# generating an identity matrix
z1 = np.identity(5)
print('\n Identity Matrix of shape {}'.format(z1.shape))
print(z1)

# be careful when you copy array
a = np.array([1,2,3,4])
b = a.copy() # to create a deep copy hence a and b are independent of each other changes

#%%
# mathematics operation
a = np.random.randint(1, 100, size=(3,6))
b = np.random.randint(1,100, size=(3,6))

print('\nArray A ')
print(a)
print('\nArray B')
print(b)

# addition
addition = a + b
print('\nAddition')
print(addition)

# multiplication --> similarly division and subtraction can be performed
# Note: the operations are element wise
multiplication = a * b
print('\nMultiplication')
print(multiplication)

# cosine --> input is considered in radians
cosine = np.cos(a)
print('\n Cosine of A')
print(cosine)

# power
value = 3
power = a**value
print('\nPower of {}'.format(value))
print(power)

#%%
# Linear Algebra

# for matrix multiplication use matmul
a = np.random.randint(1,10, size=(2,3))
b = np.random.randint(1, 10, size=(3,2))

print('\nArray A ')
print(a)
print('\nArray B')
print(b)

# matrix multiplication
matmul = np.matmul(a,b)
print('\nMatrix multiplication of A and B')
print(matmul)

# getting the determinant of matrix
a = np.random.randint(1, 10, size=(3,3))
det = np.linalg.det(a)
print('\nDeterminant using np.linalg.det(a)')
print(det)

# inverse of a square matrix
a = np.random.randint(1, 10, size=(3,3))
print('\nMatrix A')
print(a)
inverse = np.linalg.inv(a)
print('Inverse of Matrix A')
print(inverse)

# transpose of a matrix
a = np.random.randint(1, 10, size=(3,8))
print('\nMatrix A')
print(a)
transpose = np.transpose(a)
print('Transpose of Matrix A')
print(transpose)

#%%

# performing statistics in numpy
np.random.seed(42)
a = np.random.randint(1,10, size=(2, 3, 4, 5))
print('\nArray A')
print(a)

# min
a_min = np.min(a)
print('\nMinimum in A in whole A')
print(a_min)

a_min = np.min(a, axis=0)
print('\nMinimum in A at axis 0')
print(a_min)

print('sum around axis = 0')
print(np.sum(a, axis=2))

#%%

# reorganizing array
a = np.random.randint(1, 10, size=(3,3,3))
print('\nBefore Organizing')
print(a)

b = a.reshape((9,3))
print('\nAfter Organizing')
print(b)

# stacking arrays vertically
a= np.random.randint(1,10, size=(3,3))
b = np.random.randint(1, 10, size= (4,3))

print('\nArray A ')
print(a)
print('\nArray B')
print(b)

vertical_stack = np.vstack([a,b])
print('\nVertical Stack')
print(vertical_stack)

# horizontal stack
a= np.random.randint(1,10, size=(3,8))
b = np.random.randint(1, 10, size= (3,7))

print('\nArray A ')
print(a)
print('\nArray B')
print(b)
horizontal_stack = np.hstack([a,b])
print('\nHorizontal Stack')
print(horizontal_stack)

#%%
# working with range:
np_range = np.arange(0,40,5) # 0 to 10 with step size of 5
print(np_range)

# fancy indexing
indices = [1,2,-3] # index position from which other element can be taken out
y = np_range[indices]
print(y)

# manual creation of mask
mask = np.array([0,1,1,1,0,0,1,1], dtype='bool')
print(mask.size)
print(np_range[mask])

# fancy indexing in 2-D
np.random.seed(42)
two_d = np.random.randint(1,100, size=(5,5)) # 5*5 array
print('\nArray 2-D')
print(two_d)

print('Index from row 3 till last and columns 0,2,4')
print(two_d[3:,[0,2,4]])


print('Indexing 0,2,4 row and 4,3 columns')
print(two_d[[0,2,4],[0,4,3]])


#%%
# reshaping data for arange
a = np.arange(25).reshape(5,5)
print('\n (0,24) 5*5 dimension')
print(a)

#%%

a = np.arange(12).reshape(4,3)
b = np.arange(3).reshape(1,3)
print(a)
print(b)
print(a+b)

#%%
# getting the coordinates of the maximum value
np.random.seed(42)
a = np.random.randint(1,1000, size=(2, 4, 5))
print('\nArray A')
print(a)

# getting the coordinate of the maximum value in a
print('\nMaximum Values')
print(np.argmax(a, axis=0))
print('\nMaximum Values Coordinate')
print(np.where(a == np.max(a)))

#%%

# numpy reading file using loadtxt()
'''
We use loadtxt() when we have data of same type
deleimiter -- default is white space
skiprows - to the skip the n number of rows
usecols - to use the columns
'''


dataset = np.loadtxt('numpytutorial/scratch.txt', dtype=float)

print(dataset)
#%%

# genfromtxt() for reading datafile where data columns can be of different rows
# data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None) menton dtype as None for autoassin of type
# genfromtxt is a 1d array not a 2-d array. a little misleadiing


dataset = np.genfromtxt('numpytutorial/winter.csv', delimiter=',', dtype=None,
                        names=['labels','Year','City','Sport','Discipline','Athlete','Country','Gender','Event','Medal'],
                        skip_header=1)

print(dataset[[1,3,4,5,6]]['Sport'])
print(dataset[1:6]['Sport'])

# if you want a certain column use dataset[<column-name>]

# in pandas .values return the numpy array 
import pandas as pd
dataset = pd.read_csv('numpytutorial/winter.csv')
dataset = dataset.values
print(type(dataset))

#%%
#TODO: Delete code below this line

import matplotlib.pyplot as plt
import pandas as pd
help(plt.legend)
#%%

def sum_num(*args):
    print(*args)

args = [1,2,3,4,5]
kwargs = {'name':1,'age':2,'system':3}
print(len(args))

