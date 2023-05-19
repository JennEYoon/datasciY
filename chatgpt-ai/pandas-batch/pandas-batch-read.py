"""
# For use in life happiness project, batch read csv into dataframe, in chunks.  
# To save RAM memory, in future case where datafile is larger than RAM.  

Prompt: Using Pandas and Python 3, write code to read 100 line batches of csv file into a dataframe object

ChatGPT: Sure, here's some sample code to read a CSV file in batches of 100 rows using Pandas in Python 3:

In this example, we define a batch size of 100 rows and initialize an empty list to hold the dataframes. We then open the CSV file for reading and read it line by line. For each line, we check if we have reached the batch size and create a new dataframe if we have. We then parse the line into a list of values and add them to the current dataframe. Finally, we concatenate all the dataframes into one.

"""

import pandas as pd

# Define the batch size
batch_size = 100

# Initialize an empty list to hold the dataframes
dfs = []

### readline from Python built-in io. Not Pandas read_csv! ###  
# Open the CSV file for reading
with open('your_file.csv', 'r') as file:

    # Initialize a variable to keep track of the current line number
    line_num = 0
    
    # Read the file line by line
    for line in file:
        
        # Check if we have reached the batch size
        if line_num % batch_size == 0:
            
            # If we have, create a new dataframe and append it to the list
            # inner loop skipped for rows 1-99 in each batch.     
            df = pd.DataFrame(columns=['column1', 'column2', 'column3'])  
               # replace column names as per your csv
            dfs.append(df)
         
        ### next 3 lines seem redundant, reproducing Pandas functionality. ###  
        # need else?  What is preferred style?  
        # Parse the line into a list of values
        values = line.strip().split(',')
        
        # Add the values to the current dataframe
        dfs[-1] = dfs[-1].append(pd.Series(values, index=df.columns), ignore_index=True)
        
        # Increment the line number
        line_num += 1
        
# Concatenate all the dataframes into one
df = pd.concat(dfs, ignore_index=True)

"""
Prompt: Write a pandas code to read the first 100 lines from example.csv file to a DataFrame.

ChatGPT: Sure, here's the code to read the first 100 lines from example.csv file into a Pandas DataFrame:

In this example, we use the read_csv() function from Pandas to read the first 100 lines of the CSV file into a DataFrame. The nrows parameter is set to 100 to limit the number of rows read. Once the data is loaded, we can perform any data manipulation or analysis on it using the Pandas library.

"""

import pandas as pd

# Read the first 100 lines of the CSV file into a DataFrame
df = pd.read_csv('example.csv', nrows=100)

# Print the DataFrame to verify that it has been read correctly
print(df.head())

"""
Prompt: Write a pandas code to read the second 100 lines from example.csv file to a DataFrame

ChatGPT: Sure, here's the code to read the second 100 lines from example.csv file into a Pandas DataFrame:

Sure, here's the code to read the second 100 lines from example.csv file into a Pandas DataFrame:

In this example, we use the read_csv() function from Pandas to read the second 100 lines of the CSV file into a DataFrame. The skiprows parameter is set to 100 to skip the first 100 rows, and the nrows parameter is set to 100 to limit the number of rows read. Once the data is loaded, we can perform any data manipulation or analysis on it using the Pandas library.
"""

import pandas as pd

# Read the second 100 lines of the CSV file into a DataFrame
df = pd.read_csv('example.csv', skiprows=100, nrows=100)

"""
When running in batch mode, check to see if eol is reached.  
skiprows increase by multiples of 100. 
Read Pandas documentation to see what happens when eol is reached.  
rows_remaining > 100, else skiprows = current index.  
nrows=100 or rows_remaining, whichever is lesser
"""
