# numpy4, quick practice  
# Structured Arrays in numpy  
# Data start Jan 18, 2022 1:30 pm  
# Github repo: "code" folder "current" file "numpy4_structured.py"  

import numpy as np 

A = np.ones((3, 5), dtype='float32)
# expect 3 row x 5 col matrix of floating point 1.'s.  

B = np.random.random((3, 5), dtype='float16') 
# expect 3 row x 5 col matrix, random numbers (0, 1) uniform distribution  
            
C = np.random.normal((3, 3), (0, 3), dtype='float16')      
# expect 3 x 3 matric, random numbers from (mu=0, sigma=+/- 3) normal distribution  
            
# Structured Array data type  
# Only data type that can have strings in a numpy cell.
            
data = {'person':['Mary', "Jisoo", "Kevin", "Craig"], 
        'weight':[125.5, 105.3, 163.2, 180.9], 
        'id':[101, 102, 55, 56]}

mat = np.structured(data=data, dtype={'person': 'string', 'age':'float16', 'id':'uint'})     
# Not sure about name of function for structured array  
# Not sure about format            

            
            
