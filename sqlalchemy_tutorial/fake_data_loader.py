from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:system@localhost/test')
print('connected')
#%%
import pandas as pd

data = pd.read_csv('sqlalchemy_tutorial/fake.csv', header=0, names=['id','firstname','lastname'])

#%%
# Retrieving data from existing table using automap_base()
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()
Base.prepare(engine, reflect=True)

Users = Base.classes.users
session = Session(engine)
#%%

for index, row in data.iterrows():
    session.add(Users(firstname=row['firstname'], lastname=row['lastname']))
#%%