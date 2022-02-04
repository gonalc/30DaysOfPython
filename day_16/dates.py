# Day 10: 30 Days of python programming

# Dates

# Exercises: Level 1

from datetime import datetime

'''
1. Get the current day, month, year, hour, minute and timestamp from datetime module
'''

now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
print('Day: ', current_day)
print('Month: ', current_month)
print('Year: ', current_year)
print('Hour: ', current_hour)
print('Minute: ', current_minute)

'''
2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
'''
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print('Formatted date: ', t)

'''
3. Today is 5 December, 2019. Change this time string to time.
'''
old_date = datetime(year = 2019, month = 12, day = 5)
print('Old date: ', old_date)

'''
4. Calculate the time difference between now and new year.
'''
new_year_date = datetime(year = 2022, month = 1, day = 1)
diff = now - new_year_date
print('Difference with new year: ', diff)

'''
5. Calculate the time difference between 1 January 1970 and now.
'''
init_diff = now - datetime(1970, 1, 1)
print('Initial difference: ', init_diff)