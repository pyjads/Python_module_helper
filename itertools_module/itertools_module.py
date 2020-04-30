# %%
# line printer


def printer(info):
    print('\n\n================================= {} =================================================\n\n'.format(info))

# %%


import itertools

# to get a counter starting from 0 to infinte
counter = itertools.count()  # return type is the iterator and count will start from 0 and you can use it with for loop
# or next() command

# if you want to get a counter starting from certain number
start = 10
counter = itertools.count(start=start, step=-5)  # step function is optional and can be negative

# itertools.count() can be used with zip function like
counter = itertools.count(start=start, step=-5)
l = [100, 200, 300, 400]
zipped = zip(counter, l)
print(list(zipped))

# %%
from itertools import zip_longest

# zip is used to map two list and shortest list length will be considered, Iteration continues until the longest
# iterable is exhausted

l1 = ['sanket', 'sanchita', 'rohan', 'devi', 'adarsh', 'vishnu', 'prashant', 'chirag']
l2 = [1, 2, 3, 4, 5, 6]

print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2)))

# %%

from itertools import cycle

# cycle is used as circular linked list where we can iterate through certain value over and over again

# it can be use with list, tuple, string
counter = cycle([1, 2, 3, 4])
counter = cycle(('On', 'Off'))
counter = cycle('san') # it will repeat 's' 'a' and 'n'

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# %%
from itertools import repeat

# repeat can be used to repeat single value multiple time
counter = repeat(2, times=3)  # repeat 2, 3 times-- times is optional element and if not provided repeat many times
print(next(counter))
print(next(counter))
print(next(counter))

# example
squares = map(pow, range(1, 10), repeat(2, times=3))
print(list(squares))

# %%
from itertools import starmap

'''
def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)
'''


def power(x, y):
    return x ** y


# the above example in repeat can be used with starmap as
squares = starmap(power, [(0, 2), (1, 3), (2, 2), (3, 3), (4, 2), (9, 3)])
print(list(squares))

# how *args work
# for k in [(0, 2), (1, 3), (2, 2), (3, 3), (4, 2), (9, 3)]:
#     print(*k)

# %%

from itertools import combinations, permutations

# used for getting all the possible combination

letters = ['a', 'b', 'c', 'd', 'e']
number = [0, 1, 2, 3]
names = ['sanket', 'raj']

result = combinations(letters, 3)  # produce the combination where (a,b) and (b,a) is same so only one will be mentioned
print(list(result))

# if order matters the use permutations
result = permutations(letters, 3)
print(list(result))

# for example if we want to craete 4 digit code using number where combiantion can also include same number multiple
# time

from itertools import product
# computes the cartesion product
# product(iterable, repeat=n) this is permutation with replacement
# for solution see https://www.hackerrank.com/challenges/itertools-product/problem
result = product(number, repeat=3)  # arrange numbers in group of 3
print(list(result))

# in product function we have to provide repeat argumnt, the similar function that can be used is
# combinations_with_replacement

from itertools import combinations_with_replacement

result = combinations_with_replacement(number, 4)  # arrange number in a group of 4 where each number can be used
# multiple times
print(list(result))


# for permutations with replacement use below link for solution
# https://stackoverflow.com/questions/46255220/how-to-produce-permutations-with-replacement-in-python
'''
    import itertools
    choices = [-1, 1]
    n = 3
    l = [choices] * n
    list(itertools.product(*l))
'''
# %%

letters = ['a', 'b', 'c', 'd', 'e']
number = [0, 1, 2, 3]
names = ['sanket', 'raj']

# if you want to iter through all letters, number, names you first have to craete a list add all those to a single list
# and then iter through new list, this can be solved using chain
from itertools import chain

iterator = chain(letters, number, names)
print(iterator)  # object of iterator
# print(list(iterator)) # print the complete list

# %%

# islice is used to slice the iterable object which is memory efficient

letters = ['a', 'b', 'c', 'd', 'e']
number = [0, 1, 2, 3]
names = ['sanket', 'raj']

import itertools
from itertools import islice

result = islice(letters, 1, 3)
print(list(result))

result = itertools.islice(range(10), 1, 5)  # islice take (iterable, start, stop) or (iterable, stop)

# islice is used when , suppose you have a very long iterator  which is hard to load into memory and then slicing, it can
# be costly, lets, suppose we have a file
import os

with open('collections_module/islice_text', 'r') as file:
    # file object is an iterator
    header = islice(file, 3)
    for line in header:
        print(line, end='')

#


# %%
import numpy as np

np.random.seed(42)  # seeding is done for pseudo number generator
selectors = np.random.randint(1, 10000, 50)

'''
letters = np.array(['a', 'b', 'c', 'd', 'e'])
print(selectors)
print(letters[selectors])
'''

# filterfalse work as same as filter instead of returning true value it returns false values

from itertools import filterfalse

result = filterfalse(lambda x: x > 5000, selectors)  # return an iterator
print(list(result))

# %%

# dropwhile can be used when you want to filter until the condition is met for the first time
# similar to dropwhile is takewhile but the opposite of the former

import numpy as np

np.random.seed(42)
selectors = np.random.randint(1, 10000, 50)
print(selectors)

from itertools import dropwhile

result = dropwhile(lambda x: x > 500, selectors)
print(len(list(result)))

# %%
# accumulate -- it is used to work on the iterable and is used to perform cumulative operations

import numpy as np

np.random.seed(42)
selectors = np.random.randint(1, 10, 10)
print(selectors)

from itertools import accumulate
import operator

result = accumulate(selectors, operator.mul)
print(list(result))

printer('string work')

# working with the string
selectors = np.random.choice(['a', 'b', 'c', 'f', 'g'], size=10)
print(selectors)
result = accumulate(selectors, lambda x, y: x + y)
print(list(result))

#%%

# groupby work as same as pandas.groupby
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

def get_state(person):
    return person['state']


# for groupby to work efficiently, the key has to be sorted else it will not work as expected
from itertools import groupby

result = groupby(people, get_state)
for key, group in result:
    # here group is an iterator
    #
    for g in group:
        print(key,' ', g)

#%%

# in order to create multiple copies of iterator you can use tee

import numpy as np

np.random.seed(42)  # seeding is done for pseudo number generator
selectors = np.random.randint(1, 10000, 50)

from itertools import filterfalse
from itertools import tee

result = filterfalse(lambda x: x < 500, selectors)

copy1, copy2 = tee(result) # don't use the original result iterator
print(list(copy1))
print(list(copy2))


