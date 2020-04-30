#%%
import datetime
import pytz
#%%
#create date --> datetime.date(year, month, day)
d = datetime.date(2016, 7, 24)
print(d)

#%%

#create today's date
tday = datetime.date.today()
print(tday)

#get the day
print(tday.day)

#get the month
print(tday.month)

#get the year
print(tday.year)

#%%

# weekday vs isoweekday
'''
for weekday Monday 0 Sunday 6
for isoweekday Monday 1 Sunday 7
'''
tday = datetime.date.today()
print(tday.weekday())
print(tday.isoweekday())

#%%

#time delta
tday = datetime.date.today()
tdelta = datetime.timedelta(hours=7)
print(tday + tdelta)

#%%
'''
date = date1 + timedelta
timedelta = date1 + date2
'''

mybday = datetime.date(2020, 6, 25)
tday = datetime.date.today()
till_bday = mybday - tday
print(till_bday.total_months())

#%%
'''
working with time

t = datetime.time(9,30,45, 100000)
'''

t = datetime.time(9,30, 45, 10000)
print(t.second)
print(t.hour)
print(t.minute)
print(t.microsecond)

#%%
# working with datetime.datetime

t = datetime.datetime(2016, 7, 26, 1, 30, 45, 10000)
print(t.hour)

#%%

# working with timedelta and datetime
t = datetime.datetime(2016, 7, 26, 1, 30, 45, 10000)
tdelta = datetime.timedelta(days=7)
print(t + tdelta)

#%%
import pytz

#working with datetime.datetime and today

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today) # gives current datetime
print(dt_now)  # also gives current datetime but you can add timezone as well
print(dt_utcnow) # current utctime

#%%

#working with pytz

dt = datetime.datetime(2016,7,27, 12, 30, 45,  tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)


#%%

#converting utc time to local time zone
dt_utcnow = datetime.datetime.now(tz=pytz.timezone('Europe/Berlin'))
dt_mtn = dt_utcnow.astimezone((pytz.timezone('Asia/Kolkata')))
print(dt_mtn)

#%%

# all_timezones_set and country_timezones
from pytz import all_timezones_set, country_timezones, all_timezones
# print(all_timezones_set)

print(country_timezones('DE'))

# print(all_timezones)

#%%

#navie datetime
eu_tz = pytz.timezone('Europe/Berlin')
dt_mtn = datetime.datetime.now() # this is a naive datetime which is not aware of the timezone
dt_mtn = eu_tz.localize(dt_mtn) # by using localize we assign time zone to dt_mtn

print(dt_mtn)


dt_india = dt_mtn.astimezone(tz=pytz.timezone('Asia/Kolkata')) # now we convert dt_mtn to indian time zone
print(dt_india)

#%%

# format the code
eu_tz = pytz.timezone('Europe/Berlin')
dt_mtn = datetime.datetime.now() # this is a naive datetime which is not aware of the timezone
dt_mtn = eu_tz.localize(dt_mtn) # by using localize we assign time zone to dt_mtn

#isoformat
print(dt_mtn.isoformat())

#own string format
print(dt_mtn.strftime('%B %d, %Y'))

#%%
#converting string to datetime

dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)