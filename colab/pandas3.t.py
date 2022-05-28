# pandas transpose, quick exercise  
# Jan 20, 2022 12pm  
# Do some exercises to transpose Series, then see if they can be readin as columns?  
# Series are normally read in as rows, but maybe create numpy row transpose and read in together?  
# Maybe dictionary is the approved method to readin as columns.  
# Read Pandas documentation.  

import numpy as np
import pandas as pd  

col1 = np.arange(10, 15, 1).T
col2 = pd.Series(['h', 'e', 'l', 'l', 'o']).T  
print(col1, col1.shape())  # expect 5,1
print(col2, col2.shape())  # dimension?  not sure if this will work.  


df = pd.DataFrame(data=[col1, col2], columns=['A', 'B'])
# might still not work after each input columns have been transposed.  
print(df)
