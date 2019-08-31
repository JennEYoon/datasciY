


import importlib.reload(test)

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
# but then n is no longer a variable.