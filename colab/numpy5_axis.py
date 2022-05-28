# numpy axis=0 and axis=1, quick exercise 
# Jan 22, 2022 Sat 8pm  
# from Chollet chp4  

import numpy as np  
import matplotlib.pyplot as plt  

data = np.arange(1, 9).reshape(4, 2)
print(data, data.shape, type(data))

mean0 = data.mean(axis=0) 
print(mean0)
mean1 = data.mean(axis=1)
print(mean1)  

std0 = data.std(axis=0)
print(std0)  

data2 = np.random.ranint(-10, 10, 30).reshape(10, 3)
# random syntax?  30 random integers
# syntax correct except need to specify range as well as numbers to pick.  
print(data2, data2.shape)

# calculate mean and std by columns  
# do element-wise multiplication by rows.  
