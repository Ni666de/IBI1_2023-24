import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/path/to/your/directory")
data_file = "dalys-rate-from-all-causes.csv"
dalys_data = pd.read_csv(data_file)

print(dalys_data.head())

print(dalys_data.info())

print(dalys_data.describe())

print(dalys_data.iloc[::10, 3])

afghanistan_data = dalys_data[dalys_data['Entity'] == 'Afghanistan']
print(afghanistan_data['DALYs'])

china_data = dalys_data[dalys_data['Entity'] == 'China']

mean_dalys_china = china_data['DALYs'].mean()
print(f"Mean DALYs in China: {mean_dalys_china}")
print(f"DALYs in China in 2019: {china_data.loc[china_data['Year'] == 2019, 'DALYs'].values[0]}")
is_above_mean = china_data.loc[china_data['Year'] == 2019, 'DALYs'] > mean_dalys_china
print(f"Was 2019 above or below the mean DALYs in China? {'Above' if is_above_mean else 'Below'}")

plt.plot(china_data['Year'], china_data['DALYs'], 'b+')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs in China Over Time')
plt.xticks(rotation=-90) 
plt.show()
