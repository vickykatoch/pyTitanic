import pandas as pd
from matplotlib import pyplot as plt
from os import path


file_name = path.join(path.curdir,'../../data/external/countries.csv')
df = pd.read_csv(file_name)
plt.plot(df.country, df.lifeExpectancy)
plt.show()
