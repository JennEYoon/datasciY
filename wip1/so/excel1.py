

import pandas as pd


'''
df = pd.read_excel('test1.xlsx',sheetname='Sheet1',header=0,converters={'names':str,'ages':str})
>>> df
       names ages
   0   bob   05
   1   tom   4
   2   suzy  3



'''

df = pd.read_excel('test1.xlsx', sheetname='Sheet1', header=0,          converters={'header0':str,'header1':str})