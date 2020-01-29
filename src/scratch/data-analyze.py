from os import path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_name = path.join(path.curdir,'../../data/external/FX-2019.csv')
df = pd.read_csv(file_name,names=["Date", "Time", "Open", "High", "Low","Close","Volume"])
#Merge Date & Time column into single column and convert the data type to datetime
df["DateTime"] = pd.to_datetime(df["Date"].str.cat(df["Time"],sep=" "))

#Delete Date & Time Columns
df.pop("Date")
df.pop("Time")
# Bring DateTime column to the beginning
df = df[["DateTime", "Open", "High", "Low","Close","Volume"]]

open_prices = df["Open"].values
print('Mean : {}'.format(np.mean(open_prices)))
print('Median : {}'.format(np.median(open_prices)))
print('StdDev : {}'.format(np.std(open_prices)))
print('Variance : {}'.format(np.var(open_prices)))
print('Variance : {}'.format(np.sqrt(np.var(open_prices))))