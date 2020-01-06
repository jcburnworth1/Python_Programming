## Import libraries
import pandas as pd
import matplotlib.pyplot as plt

## Import the data
ad_clicks = pd.read_csv('Python_Programming/plotting/shoefly/ad_clicks.csv')

## Examine the first rows of ad_clicks
print(ad_clicks.head(10))

## Platforms getting the most views
utm_source_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()

## Add column for clicked add
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.isnull()

## Percent of each source
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

## Pivot the data
clicks_pivot = clicks_by_source.pivot(
    columns='is_click',
    index='utm_source',
    values='user_id').reset_index()

## Add click percentages to clicks_pivot
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

## Analyze the A/B Test
## Were the same number of people shown both adds?
balance_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

## Did Ad A or Ad B get more clicks?
a_vs_b = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()

## Clicks per week
a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A']

b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B']

## Calculate percentage clicked by day for each experiment
a_clicks_by_day = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()

b_clicks_by_day = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()

## Pivot a_clicks_by_day & b_clicks_by_day
a_clicks_by_day_pivot = a_clicks_by_day.pivot(
    columns='is_click',
    index='day',
    values='user_id').reset_index()

b_clicks_by_day_pivot = b_clicks_by_day.pivot(
    columns='is_click',
    index='day',
    values='user_id').reset_index()

## Percent clicked by day
a_clicks_by_day_pivot['percent_clicked'] = a_clicks_by_day_pivot[True] / (a_clicks_by_day_pivot[True] + a_clicks_by_day_pivot[False])

b_clicks_by_day_pivot['percent_clicked'] = b_clicks_by_day_pivot[True] / (b_clicks_by_day_pivot[True] + b_clicks_by_day_pivot[False])

## Plot trending percentage
a_clicks_by_day_pivot.plot(kind='line', x='day', y='percent_clicked')

plt.title('Ad A Trending')
plt.xlabel('Day')
plt.ylabel('Click %')
plt.show()

b_clicks_by_day_pivot.plot(kind='line', x='day', y='percent_clicked')

plt.title('Ad B Trending')
plt.xlabel('Day')
plt.ylabel('Click %')
plt.show()