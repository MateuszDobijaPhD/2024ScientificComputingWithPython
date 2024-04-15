# EXERCISE 5.2
#
# Create the function print_working_days(date1, date2), where 'date1' and 'date2' are strings of the form 'YYYY-MM-DD'. The function prints dates of working days (from Monday to Friday) in the given range, 'date2' is excluded.

import datetime

def isDateWorkingDay(date):
    if date.weekday() < 5:
        return True
    return False

def print_working_days(date1, date2):
    year1, month1, day1 = date1.split('-')
    year2, month2, day2 = date2.split('-')

    minDate = datetime.date(int(year1), int(month1), int(day1))
    maxDate = datetime.date(int(year2), int(month2), int(day2))
    timeDelta = maxDate - minDate

    for i in range(timeDelta.days):
        day = minDate + datetime.timedelta(days=i)
        if isDateWorkingDay(day):
            print(day)

date1 = "2024-04-01"
date2 = "2024-04-30"

print("Working days between dates:", date1, date2)
print_working_days(date1, date2)