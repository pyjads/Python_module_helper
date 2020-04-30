#%%
# import sqlalchemy
import sqlalchemy

#checking the version of sqlalchemy
print(sqlalchemy.__version__)

#%%
# connecting to sqlalchemy -- for this we need psycopg2
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:system@localhost/test')
print('connected')

#%%
# creating a table user
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()


class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))


class Account(Base):
    __tablename__='account'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))


Base.metadata.create_all(engine)

#%%
# creating the session
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

# you can also make Session = sessionmaker() and Session.configure(bind=engine)
session = Session()

#%%
#add_all command
session.add_all([User(firstname='wendy', lastname='Wendy Williams'), \
User(firstname='mary', lastname='Mary Contrary'),
User(firstname='fred', lastname='Fred Flintstone')])

# don't forget to session.commit() to commit the changes
# you can use session.dirty or session.new to check the updated data or new data which is ready to be committed
#%%

# querying the database
for instance in session.query(User):
    print(instance.firstname,' ', instance.lastname)

#%%

#querying the database
for first, last in session.query(User.firstname, User.lastname).all():
    print(first, ' ',last)
#%%

for row in session.query(User, User.firstname.label('username')):
    print(row.User, row.username)
#%%
#working with limit and offset
data = session.query(User).order_by(User.id.desc())[:3]

for instance in data:
    print(instance.firstname, ' ',instance.lastname)

#%%

#working with filter --> multiple filter can be used which works as and operator
data = session.query(User).filter(User.firstname =='Ari')

for instance in data:
    print(instance.firstname, ' ', instance.lastname)

#%%
# or operator
from sqlalchemy import or_
data = session.query(User).filter(or_(User.firstname.like('A%'), User.lastname.like('A%'), User.firstname.like('B%')))

for instance in data:
    print(instance.firstname, ' ', instance.lastname)

#%%

#working with filter and like -- like for case sensitive and ilike for case-insensitive

data = session.query(User).filter(User.firstname.like('A%'))

for instance in data:
    print(instance.firstname,' ',instance.lastname)
#%%
#query.scalar() --- execute Query.one() and upon success returns first column

data = session.query(User).filter(User.firstname.like('A%'))
print(data.scalar())

#%%

# you can also use text from sqlalchemy for querying database
from sqlalchemy import text

data = session.query(User).from_statement(text(r"Select * from users")).all()
for d in data:
    print(d.firstname)

#%%

from sqlalchemy import func
data = session.query(func.min(User.id)).all()
print(data)

data = session.query(User).filter(User.firstname.like('E%')).count()
print(data)

# count the number of rows in the table --> replicating select count(*) from table;
data = session.query(func.count('*')).select_from(User).scalar()
print(data)

# get the max user id where user.firstname starts from A
data = session.query(func.max(User.id)).select_from(User).filter(User.firstname.like('A%')).scalar()
print(data)

# getting the username where of the maximum id of name starting with A
id = session.query(func.max(User.id)).select_from(User).filter(User.firstname.like('A%')).scalar()
data = session.query(User.firstname).filter(User.id.in_([str(id)])).one()
print(data)

data = session.query(func.count(User.firstname), User.firstname).filter(User.firstname.like('E%')).group_by(User.firstname).count()
data = session.query(func.count('*')).select_from(User).filter(User.firstname.like('E%')).all()
print(data)

#%%
# Retrieving data from existing table using automap_base()
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
Base.prepare(engine, reflect=True)

Users = Base.classes.users

#%%

from sqlalchemy import create_engine
#connecting database
engine = create_engine('postgresql+psycopg2://postgres:system@localhost/test')

#getting the session
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


#
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship
from sqlalchemy import *

Base = automap_base()

class User(Base):
    __tablename__='users'

    # backref keyword is used to create backward relationship
    email_collection = relationship('email', backref='user')


Base.prepare(engine, reflect=True)

Email = Base.classes.email

# adding new email address and a user
'''
ramdev = User(firstname='Ramdev',lastname='Soni')
ramdev.email_collection = [Email(email_address='ramdev.somi@gmail.com')]
session.add(ramdev)
session.commit()
'''
# query username for a given email_id
# data = session.query(Email).filter(Email.email_address.like('%ramdev%')).one()
# print(data.user.firstname)

#query user for all the emails for a particular users staritng firstname is A
data = session.query(User).filter(User.firstname.like('A%')).all()
print(data)

for d in data:
    for i in d.email_collection:
        print(i.email_address)

# One to Many relationship
data = session.query(User).filter(User.id == str(1)).all()
print(data[0].email_collection[0].email_address)