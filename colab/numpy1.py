# Numpy1 practice 

import numpy as np

a_array = np.arange(1, 6)
print(type(a_array), a_array)

b_array = np.arange(11, 16) 
print(type(b_array), b_array)

result = a_array + b_array  
# expect element wise addition: (12, 14, 16, 18, 20) of type ndarray 
print(result, type(result), len(result))

"""
"np.arange(start, stop-1, step)" works.  
But also practice how to use "AsArray" and full spelled out list.  
Good example to use with learning debuggervin VS Code. 
Start conda session on Unix, then switch working directory to C:/repos.  

"""
