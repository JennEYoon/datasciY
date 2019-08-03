# Stackoverflow newbie question.
# How to change data type of one column in a dataframe.
# 7/7/2019 ~ 11pm

import pandas as pd

mydic = {
    "name": ['Alice', 'Tommy', 'Jane'],
    "age": [9, 21, 22],
    "height": [3.6, 6.1, 5.5],
}

df = pd.DataFrame(data = mydic)
print(df)
print(df.dtypes)

# First change age from integer to floating point.
df.age = df.age.astype('float64')

print(df.age)  # Notice the decimal format 9.0.
print(df.dtypes)  # age is now floating point.

# Next change height from floating point to integer.
df.height = df.height.astype('int32')
print(df.height)  # Notice height is truncated, no more decimal point.

# Next change age to string (object type).
df.age = df.age.astype('str')
print(df.dtypes)
print(df)

# Change height from integer to float, using bracket notation.
df['height'] = df['height'].astype('float32')
print(df.dtypes)

