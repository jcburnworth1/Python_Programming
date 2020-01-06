import pandas as pd
import numpy as np
from Python_Programming.basic_python.weather_analysis.weather_data import london_data

# print(london_data.head(10))
# print(len(london_data))

temp = london_data['TemperatureC']

average_temp = np.mean(temp)

temparature_var = np.var(temp)

temperature_standard_deviation = np.std(temp)

june = london_data[london_data['month'] == 6]['TemperatureC']

print(june)

july = london_data[london_data['month'] == 7]['TemperatureC']

print(july)

june_avg = np.mean(june)
july_avg = np.mean(july)

print("June Average Temp: {0}".format(june_avg))
print("July Average Temp: {0}".format(july_avg))

june_std = np.std(june)
july_std = np.std(july)

print("June STD Temp: {0}".format(june_std))
print("July STD Temp: {0}".format(july_std))
