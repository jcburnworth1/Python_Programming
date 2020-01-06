## Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

## Capture all state files
state_files = glob.glob('us_census_data/states*.csv')

## Loop over state_files & add to state_list
state_data = []

for file in state_files:
    data = pd.read_csv(file)
    state_data.append(data)

## Convert list of data to data frame
census_data = pd.concat(state_data)
census_data = census_data[['State', 'TotalPop', 'Hispanic', 'White', 'Black',
                           'Native', 'Asian', 'Pacific', 'Income', 'GenderPop']]

## Review columns & data types
print(census_data.columns)
print(census_data.dtypes)
print(census_data.head())

## Convert Income column to numeric
census_data['Income'] = pd.to_numeric(census_data.Income.str.replace('\$', ''))

## Fix PopulationGender Column
## Convert to columns - Men & Women
census_data['Men'] = pd.to_numeric(census_data.GenderPop.str.split('_', expand=True)[0].str.replace('M',''))
census_data['Women'] = pd.to_numeric(census_data.GenderPop.str.split('_', expand=True)[1].str.replace('F',''))

## Fill in missing Women values
census_data = census_data.fillna(value={"Women": census_data.TotalPop - census_data.Men})

## Check duplicates
duplicate_check = census_data.duplicated()

## Scatter plot of Income vs. Women
plt.scatter(census_data.Women, census_data.Income)
plt.show()