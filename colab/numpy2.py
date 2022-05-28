# Quick review Numpy  
# Dec 10, 2021 10:45 am  
#

import numpy as np  

A = np.array([5, 6, 7, 8, 9])
B = np.arange(0, 15, 3)  

print("Two arrays formed using np.array and np.arange = ", A, B)
print("dtype A =", dtype(A), "dtype B =", dtype(B))

def test1(A, B):
    # expect A = [5, 6, 7, 8, 9], dtype = ndarray
    print("Test A type, A data \n")
    print("A type match = ", bool(dtype(A)==ndarray)
    print("A data match = ", list(A)==[5, 6, 7, 8, 9])
    # expect B = [0, 3, 6, 9, 12], dtype = ndarray
    print("Test B type, B data \n")
    print("B type match =", bool(dtype(B)==ndarray)
    print("B data match =", bool(list(B)==[0, 3, 6, 9, 12]))           
             
# run test1  
test1(A, B)  
print("Test1 finished")
          
