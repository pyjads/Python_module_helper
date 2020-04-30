#%%
import pandas as pd
import numpy as np
series = pd.Series([1,2,3,4,5,6,7,8,100], index=['A','B','C','D','E','F','G','H','I'], name='Numbers' )

print(series.agg(np.mean))