import numpy as np
import pandas as pd
import datetime
from datetime import date, time, timedelta

df = pd.read_csv('test.csv')

#Converting strings to date and time
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'])

df['Date'] = df['Date'].datetime.date
df['Time'] = df['Time'].datetime.time

start_date = datetime.date(2014, 3, 3)
end_date = datetime.date(2014, 3, 4)

day_i = df.loc[df['Date']==start_date]

start_time = day_i['Time'][0]

end_time = start_time + timedelta(seconds=60)

interval_i = day_i.loc[(day_i['Time'] >= start_time) & (day_i['Time'] <= end_time)]

