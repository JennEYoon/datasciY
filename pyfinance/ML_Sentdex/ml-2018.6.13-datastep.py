##### ML Sentdex Youtube, Regression - Quandl.com data download. 
#     6/13/2018 4:45pm start  (Project started 6/11/2018 Monday)
#     continue to 2 am next day, 9h.
#     quandl.get('WIKI/GOOGL')   # Download stock data from wiki part.
#     pip install quandl to include package.
#
#     Saved Quandl downloaded data into files:
#         google_data.csv, google_data.pickle, 
#         microsoft_data.csv, microsoft_data.pickle
#
#     df.to_csv('example.csv')   # Saves to csv format.
#     df.to_pickle('example.pickle')   # Saves to binary pickle format.
#     df = pd.read_csv('example.csv')  # read data back from csv file.
#     df = pd.read_pickle('example.pickle')  # read data back from pickle file.
#
#     df.drop(columns=['B', 'C'])  # Drops columns by label.
#     df1 = df.iloc[0:rowend+1]  # truncates data rows by integer location.
#
#     Output final product files:
#         google_traindata.csv, google_testdata.csv,
#         microsoft_traindata.csv, microsoft_testdata.csv
#
#####-----#####-----#####-----#####-----#####-----#####-----#####-----#####---80

import pandas as pd
import matplotlib.pyplot as plt
import pickle
import quandl

##### Step 1 - download stock trading data from Quandl.com. #####
df1 = quandl.get('WIKI/GOOGL')
df2 = quandl.get('WIKI/MSFT')
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

##### Step 2 - Massage Data, select columns and rows. #####

### Read data back in from saved files.
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

### Next, drop rows from Microsoft, to even out time period with Google.
# 3424 data rows in Google.  Row 1 is labels.
# Google date range is 2004/08/19 to 2018/03/27.
# For Microsoft, date range is 1986/03/13 to 2018/03/27. 8076 data rows.
# Select date range from 1/1/2005 to 12/31/2017 for training ML.
# Use 3 months in 2018 for testing.
## -------------------------------------------------------------------------- ##

googla = pd.read_pickle('google_adj_data.pickle')
msfta = pd.read_pickle('microsoft_adj_data.pickle')

example = msfta.iloc[0:10, 0:5]  
# column index includes final column. row index is last-1.
# This prints 10 rows and 6 columns.
print(example)
# [start: length-1]  add 1 to last row index.
# iloc is for index by integer.  All columns are included by default.

googlat = googla.iloc[94:3365]
print(googlat.head())
print(googlat.tail())
googl_testdata = googla.iloc[3366:]
print(googl_testdata)

# Microsoft 2005-01-03 is row 4746 python convention. $20.07 Adj. Open
# Microsoft 2017-12-29 is row 8016 python convention. $85.63 Adj. Open
# Later use 'find' to search for start & end dates, rows.

msftat = msfta.iloc[4746:8017]  
msftat.head()
msftat.tail()
msft_testdata = msfta.iloc[8018:]
print(msft_testdata)

##### Step 3 - Save final massaged data to csv files for later use.
googlat.to_csv('google_traindata.csv')
msftat.to_csv('microsoft_traindata.csv')
# 3271 observations in training data for both stocks.

msft_testdata.to_csv('microsoft_testdata.csv')
googl_testdata.to_csv('google_testdata.csv')
# 58 observations in both microsoft and google test data.

# Test that written files can be re-read correctly.
# df = pd.read_csv(csv_file)
example = pd.read_csv('microsoft_testdata.csv')
print(example.tail())
