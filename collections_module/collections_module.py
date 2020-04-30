#%%
from collections import Counter

# for string
a = 'aabbbbccc'
print(Counter(a))

#for list
a = [1,2,2,1,2,3,4,1,2,3,3,23,1,123]
print(Counter(a))

#in order to get just the count number use .values()
a = 'abbbbabbbbccc'
# a = [1,2,2,1,2,3,4,1,2,3,3,23,1,123]

print(Counter(a).values())

#to get the most common used --> use .most_common(2)
print(Counter(a).most_common(2))

# to get iterator of elements
a = 'bbbabbbbabbbbccc'
iterator = Counter(a).elements() # return the iterator where all same elements are ordered together
print(list(iterator))

#%%

from collections import namedtuple

Points = namedtuple('Points', 'x,y')
pt = Points(1,-4)
print(pt)
print(pt.x)
print(pt.y)

#%%
from collections import OrderedDict

# the orderedDict will remember the order in which data is inserted
# but from python 3.7 onwards the default dict also remembers the order
ordered_dict = OrderedDict()
ordered_dict['a'] = 100
ordered_dict['b'] = 120
ordered_dict['c'] = 50
ordered_dict['d'] = 180
ordered_dict['e'] = 350

print(ordered_dict)

#%%
from collections import defaultdict

# defaultdict is similar to normal dictionary but it will have default value

d = defaultdict(int) # you can also define the type you can use float, str, list etc. if the key does not exist then it
# will create with default creation you have provided in defaultdict
d['a'] = 100
d['b'] = 120
d['c'] = 50

print(d)
print(d['m'])
print(d) # if you try to access any value that is not in defaultl_dict then it will create a key and store default value

#%%
from collections import deque

# can be used as queue where we can access value either from first or last

d = deque()
d.append(1) # first element added
d.append(2) # second element will be added to the right end

d.appendleft(4) # will be appended at the beginning
print(d)

print(d.pop()) # will pop from the right end

print(d.popleft()) # will return and remove the element from the beginning

d.extend([1,2,3,4]) # will add all the elements at the right end
d.extendleft([100,200,300]) # will add all the elements at the left end
print('before rotation: ',d)
d.rotate(1) # will rotate all the elements to the right by 1

# we can rotate to the left side as well by providing the negative number
print('after rotation: ',d)

d.clear() # to clear


#%%

from collections import ChainMap

# chainmap is used to combine multiple dictionaries to one dictionary

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
chainmap = ChainMap(adjustments, baseline)
print(chainmap['music'])

