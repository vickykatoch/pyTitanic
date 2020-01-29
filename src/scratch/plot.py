import pandas as pd
from matplotlib import pyplot as plt
from os import path


# file_name = path.join(path.curdir,'../../data/external/countries.csv')
print(path.curdir)
file_name = '..\\..\\data\\external\\countries.csv'
# pd.read_csv(file_name)
print(file_name)
print(path.exists(file_name))
