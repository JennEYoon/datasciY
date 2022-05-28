"""
# short practice 
# Nov 29, 2021 missed github day
#  
# 1) loop list a and list b with zip  
# 2) then use numpy to do the same  
"""

a_list = [11, 12, 13, 14, 15]
b_list = [1, 2, 3, 4, 5]

# test len(a)==len(b)
print("length test a==b ?", len(a_list), len(b_list), bool(len(a_list)==len(b_list)))
# need to convert type to "bool" to show equality true/false.  

#  first try, get index errors.  
#result = []
#for i in a_list:  
#    for j in b_list:
#        result = [i+j for i, j in zip(a_list[i], b_list[j])]
#        print(result)
# does this return a list or one element summed?  
# do I need to append each item to list?
#print("element wise sum of a and b?", result)

#  try again without looping, indexing  
#  removed i, j from inside zip lists.  
result = []
result = [i+j for i, j in zip(a_list, b_list)]
print("result", result) 
# works!

### output
#>> length test a==b ? 5 5 True
#>> result [12, 14, 16, 18, 20]

import numpy as np
a_array = np.array([11,12,13,14,15])
b_array = np.array([1,2,3,4,5])
result = a_array + b_array  # expect ndarray(12,14,16,18,20)
print(result)  
