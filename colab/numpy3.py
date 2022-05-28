# Numpy practice 3 
# code repo, private dev  
# Jan 4, 2022  

import numpy as np  

# Create matrix  
A = np.ones().reshape(3, 3)
print(A, type(A))  
# expect ndarray type, [[1,1,1], [1,1,1], [1,1,1]]

B = np.array([1,2,3], [4,5,6], [7,8,9])
print(B, type(B)) 
# expect ndarray type, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  

print(A.shape(), B.shape())
# expect 3x3 3x3  

""" Evaluation:  
Has 1 error on each part.  
Fixed each in 1-2 tries after reading error code. 
See "code3a.ipynb"  

Worthy quick exercise, since I didn't get them correct on first try.  
Copy run on CoLab and saved back to Github, also downloaded to laptop repo directory.  
"""
