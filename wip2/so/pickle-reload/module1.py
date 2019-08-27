#!/usr/bin/env python
# coding: utf-8

# In[1]:


# notebook1_pk.ipynb

# notebook1.ipynb:
new_income_df = pd.DataFrame(data=[100, 101])
print(new_income_df)
# change one cell value and test reload.

# notebook2.ipynb
%load_ext autoreload
%autoreload 2
df2 = notebook1.ipynb.new_income_df
print(df2)
# In[13]:


# notebook1.ipynb
import pandas as pd
new_income_df = pd.DataFrame(data=[100, 101])
print(new_income_df)
# change one cell value and test reload.
# new_income_df[0][1] = 202  # 1st column, 2nd row is changed.
# print(new_income_df)


# In[3]:


new_income_df


# In[4]:


new_income_df.dtypes


# In[2]:


# File > Download As > Python (.py)
# Name the file module1.py
# Save to your working directory.


# In[ ]:




