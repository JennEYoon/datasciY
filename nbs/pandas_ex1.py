# Simple Pandas code review, practice  
### Feb 5, 2023 Sunday 5:40 pm  
### Jennifer E Yoon author  
### Env: ROG conda3 base, python 3.9, ds libraries

import numpy as np
import pandas as pd 
from pandas import Series, DataFrame

### index as immutable array, p 106 VanderPlas 2017  
ind = pd.Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
print(ind, type(ind))

print(ind[2])   # ith item
print(ind[-1])  # last item
print(ind[::3])  # repeat every 3rd starting at 0th.  

### reversed repeat
print(ind[2::-1])  # reversed repeat, count from -2 not 0. [8, 7, 6, ...] I thinkt this is correct.  
          # or it could be reversed from 2 to 10, [10, 9, 8, .. 3, 2]
print(ind[::-1])  # this reverses the whole thing starting from last item.   
          # so likely count backwards, starting from last as 0th.  
# >>> Wrong! [2, 1, 0].  Start from ith, the reverse by step one repeatedly.  
print(ind[8::-2])   # expect [8, 6, 4, 2, 0]  Start from ith, reverse by step -n, repeat. 
          
### [i::+/-n]  Start from ith from left, then repeat (2nd :) every nth, or -nth.  
print(ind[0::-2])  # only gives "[0]"  
# so [::-1] must be a special case. if 0th is not specified, start from last.  
print(ind[::-2])  # in reverse, not specified start is same as start from last  
print(ind[-1::-2])  # count from right assumed in reverse flow, if omitted.  

### index masking, filtering  

states = pd.Series(['Virginia', "Maryland", 'California', 'Rhode Island'])
print(states)
population = pd.Series([8683619, 6164660, 39029342, 1093734])
print(population)

### https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population  
### population as of July 1, 2021. original source: US Census Quick Facts. 

table = pd.DataFrame(data=[states, population]).T
print(table)	
table.columns = ['states', 'population']
print(table)

print(table[table['population'] > 5000000])
print(table[(table['population'] < 5000000) | (table['population'] > 10000000)])
# Need parenthesis for compound filter. OR | , AND & .  

print(table[(table.population < 5000000) | (table.population > 10000000)])
# can have 1 attribute dot notation. Cannot string attribute series.  

### McKinney, Series as object with (velues, index labels)
### 2/8/2023 2 am.  

obj = Series([4, 7, -5, -3])
obj
obj[2]
obj.values # plural values.  
obj.index  # singular index.  
obj[3] = -1 
obj

obj2 = Series(data=[4, 7, -2, -5], index=['a', 'b', 'c', 'd'])
obj2.index
obj2.values
obj2

obj2['d'] = -10
obj2.a = 10
obj2

# filtering, obj2 where obj2.values > 2  
obj2[obj2 > 2]

### filtering, list of columns.  
obj2[['a', 'd', 'c']]  # need 2nd [] for multiple items list.  

# multiplication  
obj2 * 3  
      
# exponential function  
np.exp(obj2)

# x raised to y power
obj2 ** 3

obj3 = Series([-3, -2, -1, -.5, 0, .5, 1, 2, 3])
np.exp(obj3)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('qtagg')


plt.figure(figsize=(5, 5))
plt.plot(obj3.index, np.exp(obj3))
plt.title('e, exponential')
plt.show()



