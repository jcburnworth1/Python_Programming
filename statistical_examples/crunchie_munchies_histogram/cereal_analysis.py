## Import libraries
import numpy as np
from matplotlib import pyplot as plt

## Load data from cereal.csv
calories_stats = np.genfromtxt('crunchie_munchies/cereal.csv', delimiter=',')

print(calories_stats)

## Average calories
average_calories = np.mean(calories_stats)

print("Average Calories: {0}".format(str(average_calories)))

## Sort the data and see if average represents the dataset
calories_stats_sorted = np.sort(calories_stats)

print(calories_stats_sorted)

## Calculate median categories
median_calories = np.median(calories_stats)

## Historgram of calories
plt.hist(calories_stats)
plt.axvline(x=average_calories, c = 'r')
plt.axvline(x=median_calories, c = 'g')
plt.show()
plt.close('all')

## Calculate percentile above CrunchieMunchie calories
percentile_above = np.percentile(calories_stats, 5)
print(percentile_above)

## Calculate percentage of cereals > 60 calories
greater_than_60 = round(np.mean(calories_stats > 60) * 100,2)

print('{0}% of cereals have a calorie count greater than 60.'.format(str(greater_than_60)))

## Calculate STD of cereals
calories_std = np.std(calories_stats)