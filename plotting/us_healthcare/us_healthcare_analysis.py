## Import libraries
import pandas as pd
from matplotlib import pyplot as plt

## Read in the data
healthcare = pd.read_csv("Python_Programming/plotting/us_healthcare/healthcare.csv")

## Print the head of the data
print(healthcare.head(10))

## View unique diagnoses
print(healthcare["DRG Definition"].unique())

## Subset data to chest pain only
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

## Subset to Alabama for first boxplot
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == 'AL']

## Subset data to costs only
costs = alabama_chest_pain['Average Covered Charges'].values

## Plot the AL cost values
plt.boxplot(costs)
plt.show()

## Capture unique states to begin our boxplots
states = chest_pain['Provider State'].unique()
states.sort()

## Separate data into each state
datasets = []

for state in states:
    datasets.append(chest_pain[chest_pain['Provider State'] == state]['Average Covered Charges'].values)

## Setup figure size for the 50 boxplots
plt.figure(figsize=(20, 6))

## Draw our 50 boxplots
plt.boxplot(datasets, labels=states)
plt.savefig('Python_Programming/plotting/us_healthcare/state_boxplots.png')
plt.show()