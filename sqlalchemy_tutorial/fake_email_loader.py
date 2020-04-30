
#%%

from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:system@localhost/test')
print('connected')
#%%


from sqlalchemy.ext.automap import automap_base

Base = automap_base()
Base.prepare(engine, reflect=True)

Users = Base.classes.users


#%%
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(Users.id))
    email_address = Column(String, nullable=False)

Base.metadata.create_all(engine)

#%%

import pandas as pd

data = pd.read_csv('sqlalchemy_tutorial/email.csv', header=0, names=['id','email'])

#%%

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
session.rollback()
for index, d in data.iterrows():
    session.add(Email(user_id=d['id'], email_address=d['email']))

session.commit()
#%%

