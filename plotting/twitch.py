## Import libraries
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games Data
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]
viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

## Begin Bar Chart
plt.bar(range(len(games)), viewers, color="green")
plt.title('Twitch Most Viewed Games')
plt.legend(['Twitch'])
plt.xlabel('Games')
plt.ylabel('Viewers')
ax = plt.subplot()
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation=30)
plt.show()
plt.close('all')

# Pie Chart: League of Legends Viewers' Whereabouts Data
labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink',
          'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

## Begin pie chart
plt.pie(x=countries, colors=colors, explode=explode,
        shadow=True, startangle=345,
        autopct='%1.0f%%', pctdistance=1.15)
plt.title("League of Legends Viewers' Whereabouts")
plt.legend(labels, loc='right')
plt.show()
plt.close('all')

# Line Graph: Time Series Analysis Data
hour = range(24)
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

## Create bounds for viewers_hour uncertainty
y_upper = [hour * 1.15 for hour in viewers_hour]
y_lower = [hour * .85 for hour in viewers_hour]

## Being line chart
plt.plot(hour, viewers_hour)
plt.fill_between(hour, y_upper, y_lower, alpha=0.2)
plt.title("US Viewers Watching Patterns")
plt.xlabel('Hour')
plt.ylabel('Viewers')
ax1 = plt.subplot()
ax1.set_yticks(hour)
ax1.set_yticklabels([0,20,40,60,80,100,120])
plt.legend(['2015-01-0-1'])
plt.show()
plt.close('all')