import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# %%

ds = [1940,1950,1975,1999]
pop = [10,20,30,40]

plt.plot(ds, pop, marker='o')
plt.show()

#%%
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
    index=['cobra', 'viper', 'sidewinder'],
    columns=['max_speed', 'shield'])

df['add v'] = df['max_speed'] + df['shield']
td = df.loc[(df['max_speed']>=4) & (df['shield'] >= 5) & (df['add v']>=9)]
print(td)

#%%

x = [np.random.randint(0,11) for _ in range(10)]
# x=[7, 9, 0, 4, 5, 4, 1, 1, 3, 6]
print(x)
plt.hist(x,bins=10)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.show()
#%%
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# Plot histogram of ends, display plot
n,bins,patches = plt.hist(ends)
plt.show()
#%%

def sanket():
    '''This is of no use just for fun'''

help(sanket)