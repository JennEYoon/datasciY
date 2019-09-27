# Reading notes on Numpy chapter, VanderPlas.  

#### Broadcasting  

* Broadcasting is stretching the source data to fill in the destination shape.   
A = np.array([0, 1, 2])  
B = 5  

A + B is same as [0, 1, 2] + [5, 5, 5] = [5, 6, 7]  
B is stretched from [5] to [5, 5, 5]  
