## Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Read in the data
data = pd.read_csv("life_expectancy/country_data.csv")

## Print the head of the data
print(data.head(10))

## Isolate the life expectancy data
life_expectancy = data['Life Expectancy']

## Calculate quartiles
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])

## Plot a histogram of life expectancy
plt.hist(life_expectancy)

## Plot quartiles
for quartile in life_expectancy_quartiles:
    plt.axvline(x=quartile, c = 'r')
plt.show()

## Split data by gdp
gdp = data['GDP']

## Find Median GDP
median_gdp = np.quantile(gdp, 0.5)

## Split life expectancy by gdp high or low
low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]

## Calculate quartiles for low and high
low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [0.25, 0.5, 0.75])
high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'], [0.25, 0.5, 0.75])

## Plot the two gdp spreads in the same view
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")

## Plot quartiles
for quartile in high_gdp_quartiles:
    plt.axvline(x=quartile, c = 'r')

plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")

## Plot quartiles
for quartile in low_gdp_quartiles:
    plt.axvline(x=quartile, c = 'g')

plt.legend()
plt.show()
