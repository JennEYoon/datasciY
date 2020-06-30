# author:   Jennifer Yoon
# file:     module my_datetime.py
# started:  6/8/2017  5:00 PM
# stopped:  6/9/2017  3:30 AM
#-----------------------------------------------------------------------

import time
now = time.strftime("%c")
print(now)

weekday = time.strftime("%a")  # %a is short, %A is full.
date = time.strftime("%m/%d/%Y")  # MM/DD/YYYY.
timef = time.strftime("%I:%M %p")  # HH:MM AM/PM.

nowf = [weekday, date, timef]
print(nowf)