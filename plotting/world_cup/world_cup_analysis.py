## Import Needed Libraries
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

## Read in the data
world_cup_matches = pd.read_csv('world_cup/WorldCupMatches.csv')
goals = pd.read_csv('world_cup/goals.csv')

## Inspect world_cup_matches dataframe for clarity
print(world_cup_matches.head(5))

## Inspect goals for clarity
print(goals.head(5))


## Add new column - Total Goals
world_cup_matches['Total Goals'] = world_cup_matches['Home Team Goals'] + world_cup_matches['Away Team Goals']

## Check that column was added
if world_cup_matches.columns.contains('Total Goals'):
    print('Successful')
else:
    print('No Column Exists')

## Plot goals by year for WC Matches
sns.set_style('whitegrid')
sns.set_context('poster')
f, ax = plt.subplots(figsize=(12,7))
ax = sns.barplot(data=world_cup_matches, x='Year', y='Total Goals', ci=None, estimator=sum)
ax.set_title('World Cup Total Goal by Year')
plt.show()
plt.close('all')

## Plot Distribution of Goals
sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12,7))
ax2 = sns.boxplot(data=goals, x='year', y='goals', palette='Spectral')
ax2.set_title('Goal Distribution by Year')
plt.show()
