# Reading notes on Numpy chapter, VanderPlas.  

#### 1. Broadcasting  

* Broadcasting is stretching the source data to fill in the destination shape.   
A = np.array([0, 1, 2])  
B = 5  

A + B is same as [0, 1, 2] + [5, 5, 5] = [5, 6, 7]  
B is stretched from [5] to [5, 5, 5]  

#### 1. Masks, Fancy Indexing  

list = ["Mary", "Tom", "Harry", "Moe"]  
ind = [1, 2]  
A = np.array(list)  # Convert list data to ndarray abject.
B = np.array(A[ind])  
B = ["Tom", "Harry"]  

