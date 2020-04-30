#%%
import calendar
#%%

c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2008,1)
print(st)

#%%

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2017,8):
    print(i)

#%%
for i in calendar.month_name:
    print(i)

for day in calendar.day_name:
    print(day)
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms

#%%
# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
cal = calendar.monthcalendar(2018,1)
print(calendar.FRIDAY)
print(cal)
print("Team meeting will be on:")
for m in range(1,13):
    cal = calendar.monthcalendar(2018,m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] !=0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))


#%%

# to get the range of the month use monthrange()
# (2, 30) specify the weekday ie Wednesday (day for 1st of the month) and total days in the month
print(calendar.monthrange(2020, 4))