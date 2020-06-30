##### ML Sentdex Youtube, Regression - Quandle data download. 
#     6/13/2018 4:45pm start  (Project started 6/11/2018 Monday)
#     quandl.get('WIKI/GOOGL')   # Download Google data from wiki part.
#     df.to_csv('example.csv')   # Saves to csv format.
#     df.to_pickle('example.pickle')   # Saves to binary pickle format.
#     with open('mypickle.pickle', 'wb') as f:
#         pickle.dump(some_obj, f)
#     with open('mypickle.pickle', 'rb') as f:
#         loaded_obj = pickle.load(f)
#     df.drop(columns=['B', 'C'])  # Drops columns by label.
#####-----#####-----#####-----#####-----#####-----#####-----#####-----#####---80

import pandas as pd
import matplotlib.pyplot as plt
import pickle
import quandl

##### Step 1 - download stock trading data from Quandl.com. #####
# df1 = quandl.get('WIKI/GOOGL')
# df2 = quandl.get('WIKI/MSFT')
### GOOGL is non-voting C shares, while GOOG is voting A shares.

# Inspect downloaded data. #
print('Google stock prices, head & tail:')
df1.head()
df1.tail()
print('Microsoft stock prices, head & tail:')
df2.head()
df2.tail()

# Save data to csv and binary files for re-use. #

# save dataframe to csv file.
df1.to_csv('google_data.csv')
df2.to_csv('microsoft_data.csv')

# Save dataframe to binary file using pickle.
df1.to_pickle('google_data.pickle')
df2.to_pickle('microsoft_data.pickle')
df1r = pd.read_pickle('google_data.pickle')
df2r = pd.read_pickle('microsoft_data.pickle')
df1r.tail()
df2r.tail()

# Alternative pickle example, best for dictionary data not in dataframe. #
with open('stock1_data.pickle', 'wb') as f1:
    pickle.dump(df1, f1)
with open('stock1_data.pickle', 'rb') as f1:
    data1 = pickle.load(f1)
print('loaded_obj is', data1.tail())

### Reading stock data back in from saved binary files. ###
googl = pd.read_pickle('google_data.pickle')
print(googl.tail())
# Drop unwanted columns
googl = googl.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume', 
    'Ex-Dividend','Split Ratio'])
print(googl.tail())

msft = pd.read_pickle('microsoft_data.pickle')
print(msft.tail())
msft = msft.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume', 
    'Ex-Dividend','Split Ratio'])
print(msft.tail())

msft.to_pickle('microsoft_adj_data.pickle')
googl.to_pickle('google_adj_data.pickle')
msft.to_csv('microsoft_adj.csv')
googl.to_csv('google_adj.csv')

##### Next, drop rows from Microsoft, to even out time period with Google.
# 3424 data rows in Google.  Row 1 is labels.
# Google date range is 2004/08/19 to 2018/03/27.
# For Microsoft, date range is 1986/03/13 to 2018/03/27. 8076 data rows.
# Select date range from 1/1/2005 to 12/31/2017 for training ML.
# Use 3 months in 2018 for testing.
## -------------------------------------------------------------------------- ##

