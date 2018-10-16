"""
IICV Cookbook - My Work Titanic data

Author: Jennifer Yoon  
Date: 9/13/2018 start, 9/18, 9/19, 9/20 continue  
File: titanic-part1-v3.py as edited in VS Code.
Path: c:\python\iicv\  
Settings: c:\python\conda3\python.exe.  Miktex works in this environment.  
  
Description: A Reproduction work based on a book by Cyrille Rossant.  
Citation: Rossant, Cyrille, IPython Interactive Computing and Visualization Cookbook,
2nd ed., Packt Publishing, 2018, ISBN 978-1-78588-863-2 (p 299-304). 
"""

#### Titanic ML example ####

import numpy as np
import pandas as pd
import sklearn
import sklearn.linear_model as lm
import sklearn.model_selection as ms
import matplotlib.pyplot as plt

### Load training datasets using Pandas dataframe object. ###

# Input parameters.
param1 = ('https://github.com/ipython-books'
         '/cookbook-2nd-data/blob/master/'
         'titanic_train.csv?raw=true')
print("param1:\n", param1)

param2 = ('https://github.com/ipython-books'
         '/cookbook-2nd-data/blob/master/'
         'titanic_test.csv?raw=true')
print("param2:\n", param2)

# Commands.
train = pd.read_csv(param1)
test = pd.read_csv(param2)
train[train.columns[[2, 4, 5, 1]]].head()

print(len(train.columns))
print(len(train))
print(type(train))

# Dataframe has 12 columns, 891 rows, and is a DataFrame type.
train.head()

### Descriptive statistics on training data. ###
# Average, stdev, min, max, count, nas.

### Manipulate DataFrame Object. ###

# Select fields, convert sex field to binary, remove rows with NaN values.
data = train[['Age', 'Pclass', 'Survived']]
print(data.head())

# Add a female binary sex column.
data = data.assign(Female = train['Sex'] == 'female')
print(data.head())

# Reorder the columns.
data = data[['Female', 'Age', 'Pclass', 'Survived']]

# Drop rows with NaN, missing values.
data = data.dropna()
print("Rows remaining in training data after dropping na:", len(data))
data.head()

# Convert data object from Pandas DataFrame to NumPy array 
# inorder to use it in Scikit-Learn. 
datanp = data.astype(np.int32).values
X = datanp[:, :-1]  # Selects all columns except last column. Capital X.
Y = datanp[:, -1]   # Selects last column only. Capital Y.
print("X 2d array, 'Femake, Age, Pclass':", X[0:5])
print("Y 1d array, 'Survived':", Y[0:5])

# Check that the number of rows is unchanged from before conversion.
len(datanp)  

#### Graphing Male & Female Survivors. ###

# We define a few boolean vectors.

# The first column is 'Female'.
female = X[:, 0] == 1

# The last column is 'Survived'.
survived = Y == 1

# This vector contains the age of the passengers.
age = X[:, 1]

print(female[0:5])
print(survived[0:5])
print(age[0:5])
len(survived)

# We compute a few histograms.
bins_ = np.arange(0, 81, 5)
S = {'male': np.histogram(age[survived & ~female],
                          bins=bins_)[0],
     'female': np.histogram(age[survived & female],
                            bins=bins_)[0]}
D = {'male': np.histogram(age[~survived & ~female],
                          bins=bins_)[0],
     'female': np.histogram(age[~survived & female],
                            bins=bins_)[0]}


# We now plot the data.
bins = bins_[:-1]
fig, axes = plt.subplots(1, 2, figsize=(10, 3),
                         sharey=True)
for ax, sex, color in zip(axes, ('male', 'female'),
                          ('#3345d0', '#cc3dc0')):
    ax.bar(bins, S[sex], bottom=D[sex], color=color,
           width=5, label='survived')
    ax.bar(bins, D[sex], color='k',
           width=5, label='died')
    ax.set_xlim(0, 80)
    ax.set_xlabel("Age (years)")
    ax.set_title(sex + " survival")
    ax.grid(None)
    ax.legend()
    
   
fig.show()
































