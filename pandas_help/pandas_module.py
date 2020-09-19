import pandas as pd

#%%

'''
if you want to read a txt or any other files as pandas use below code:
    data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

'''
#%%

'''
pickle is used for saving python objects with the concept of serializing and deserializing
 opening a pickle file
 
 with open('data.pkl', 'rb') as file:
        d = pickle.load(file)
'''

#%%

# reading excel spread sheets

'''
# to read excel file use:
data = pd.ExcelFile(file)

# to see sheet names:
names = data.sheet_names

# parsing sheet:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.ExcelFile.parse.html
# check read_excel for more options
# general code
# df = data.parse(0, skiprows=[1], names=['Country','AAM due to War (2002)']) --> skiprows need to be of typle list
df1 = data.parse('sheet_names<string>')
df2 = data.parse(index_of_sheet)

'''

#%%

'''
importing SAS files


# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())
'''

#%%

# read stata files

'''
use:
pd.read_stata(<file_name>)
'''

#%%

'''
Matlab files -- scipy.io.loadmat() scipy.io.savemat()
.mat files is a collection of varaibles


import scipy.io
mat = scipy.io.loadmat(filename)
type(mat) is dict where keys are matlab variables and values are objects assigned to variables


'''

#%%

# using sqlalchemy
'''
from sqlalchemy import create_engine

engine = create_engine(<connection>)
connection = engine.connect()
rs = connection.execute(SQL_Query)
data = pd.DataFrame(rs.fetchall()) --> You can use rs.fectchmany(<number of rows to search>)
data.columns = rs.keys()


All the above steps can be done in 1 step
data = pd.read_sql_query(<query>, engine)
'''
#%%

'''
excel can be read directly from url 
excel = pd.read_excel(url, sheet_name=None)

# the above will read all the sheets 
then you can use data.keys() to see sheet names and excess sheet using excel[<sheet_name>] 
you can also use it as:
dataset = pd.DataFrame(excel[<sheet_name>]
'''