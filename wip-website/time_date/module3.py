"""
from module import var1, does NOT import module's name. NOT allow module.var2.
ONLY import module adds module's name to the namespace and allows module.var2.
"""
#---------------------------------------------------------------------
# Author:      Jennifer Yoon
# File, Path:  module3.py, C:\GDrive\Coding\Python
# Start Time:  06/09/2017  03:19
#
# timestamp -- Use now+Control+J -- PyScripter code snippet
# time:     06/09/2017  03:50
# time:     06/09/2017  14:49
#
#---------------------------------------------------------------------

# Question.  If from module import name1, then can I also use module.name2?
# Guess -- should, don't see why not.  If not, nodule __name__ is not imported.
# mytime.py has nowc statement, now() function definition names.

from mytime import now
print(now())

print(mytime.nowc)
# Wrong!  Really does not import the module name!
"""
Traceback (most recent call last):
  File "<string>", line 420, in run_nodebug
  File "C:\GDrive\Coding\Python\module3.py", line 20, in <module>
    print(mytime.nowc)
NameError: name 'mytime' is not defined
"""

print(dir())
"""
['__builtins__',
 '__doc__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'now',
 'pyscripter']
 """

# Test 2
from mytime import nowc
print(nowc)
print(mytime.now)
print(now())
# Wrong!  Really does not import the module name!
"""
Traceback (most recent call last):
  File "<string>", line 420, in run_nodebug
  File "C:\GDrive\Coding\Python\module3.py", line 20, in <module>
    print(mytime.nowc)
NameError: name 'mytime' is not defined
"""