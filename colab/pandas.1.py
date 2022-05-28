# Quick exercise, pandas library  
# Jan 10, 2022 6:40 am  

import numpy as np
import pandas as pd  
import random  

names = ["helen", "mary", "jane", "tom", "philippe", "craig"]
ids = np.arang(1000, 1006, 1)
print(names, len(names), type(names)
print(ids, len(ids), type(ids))
ids = list(ids)  # change type, needed?  
# convert to use zip and list, else dataframe directly accepts ndarray type.  
      
# df1 = pd.dataframe(data=[names, ids], cols=("names", "idnum"))
df1 = pd.DataFrame(list(zip(ids, names)), columns=["id", "name"])      
print(df1.head(6))

      
# try creating df by using one col, then adding second col.     
ids = np.arang(1000, 1006, 1)
      
df2 = DataFrame(ids)
ser = Series(names)
df2 = df2.Add(ser)     
      
# get id number of Jane 

      
      
      
# print all names 
      
      
# add sex column  
      
      
      
# print all male data rows  
      
      
      
