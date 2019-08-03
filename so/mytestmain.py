# Load file mytest.py from the working directory.
# This file is "mytestmain.py", also in working directory.

import mytest
# output: <module 'mytest' from 'c:\\python\\so\\mytest.py'>

data1 = 2
answer1 = 4 

data2 = 3
answer2 = 10 

# Call function "test" inside "mytest.py" module.
# Function "test" calculates a square of a number.

# Test1 with data1, which is 2. Answer is 4.
# This is the correct answer, test should pass.
result = mytest.test(data1, answer1)
print("Result1: ", result)

# Test2 with data2, which is 3.  Answer is 9.
# This is the wrong answer, test should fail.
result = mytest.test(data2, answer2)
print("Result1: ", result)

""" ###########################

if n = 0:
       import(test)
   n=n+1
else: 
    reload(test)

    n = 1
import test as n
n=n+1



##########################################################
''' I have a basic tool with a Tkinter GUI that loops through a line test and then allows to do a test on a new service through a separate testing module. I had an issue with the retest just giving the same data as the previous so added importlib.reload(test) which solved that problem, but now the code runs through twice. '''

# I have tried adding a counter like this

if n = 0:
   import(test)
   n=n+1
else: 
    reload(test)

# but on the second loop I get error
###  UnboundLocalError: local variable 'test' referenced before assignment

# I need the test to run through once and then reload on the second test with fresh
# data

n = 1
import test as n
n=n+1
# but then n is no longer a variable. """