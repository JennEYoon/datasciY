# author:   Jennifer Yoon
# file:     mytime.py  C:\GDrive\Coding\Python
# started:  6/8/2017  5:00 PM
# stopped:  6/9/2017  3:30 AM
#-----------------------------------------------------------------------

import time
nowc = time.strftime("%c")
print(nowc)

def now():
    #returns date & time formatted to my preference.
    weekday = time.strftime("%a")  # %a is short, %A is full.
    date = time.strftime("%m/%d/%Y")  # MM/DD/YYYY.
    timef = time.strftime("%I:%M %p")  # HH:MM AM/PM.
    result = [weekday, date, timef]
    return(result)

#print(now())
# time:     06/09/2017  03:50
# time:     $[DateTime-'MM/DD/YYYY  HH:NN'-DateFormat]
# Not sure how PyScripter enters current system time into a script file.