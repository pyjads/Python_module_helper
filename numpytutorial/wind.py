import numpy as np

wind_data = np.loadtxt('numpytutorial/scratch.txt')

#%%

months = (wind_data[:, 0] - 61) * 12 + wind_data[:, 1] - 1
print(months)