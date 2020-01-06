##### Scrape a web page and extract an embedded table
## Import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

## Flavors of Cacao Rating System:
## 5= Elite (Transcending beyond the ordinary limits)
## 4= Premium (Superior flavor development, character and style)
## 3= Satisfactory(3.0) to praiseworthy(3.75) (well made with special qualities)
## 2= Disappointing (Passable but contains at least one significant flaw)
## 1= Unpleasant (mostly unpalatable)

##### Capture the webpage and its content #####
## Request the webpage
webpage = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
webpage_content = webpage.content

## Create a soup object to start pulling the data
chocolate_soup = BeautifulSoup(webpage_content, 'html.parser')
# print(chocolate_soup)

## Clean up
del(webpage, webpage_content)

##### Capture the table in its entirety #####
## Find the table based on tag and attribute
ratings_table = chocolate_soup.find('table', attrs={'id':'cacaoTable'})

## Clean up
del(chocolate_soup)

##### Parse out the specific data elements #####
## Parse out the various columns
## Creat a function to grab the data
def get_chocolate_table_data(table, tag, attrs):
    """ Function will take the passed html table, and return the text for a given tag & attribute combination"""
    """## Example
       ## ratings_table_company = ratings_table.find_all('td', attrs={'class':'Company'})
       ## ratings_table_company_text = ratings_table_company[0].get_text()"""
    temp_data = table.find_all(tag, attrs)
    temp_list = []

    for each in temp_data:
        temp_list.append(each.get_text())

    return temp_list

## Headers list for searching the ratings_table
headers = ['Company','Origin','REF','ReviewDate','CocoaPercent',
           'CompanyLocation','Rating','BeanType','BroadBeanOrigin']

## Empty list to capture all columns in a separate nested list
table_data = []

## Loop over headers & get all columns
for header in headers:
    temp_list = get_chocolate_table_data(ratings_table, 'td', {'class':header})
    table_data.append(temp_list[1:])

## List to dataframe
chocolate_df = pd.DataFrame.from_records(table_data).transpose()
chocolate_df.columns = headers

## Clean up
del(header, headers, ratings_table, table_data, temp_list )

## Update column types
chocolate_df['REF'] = pd.to_numeric(chocolate_df.REF)
chocolate_df['ReviewDate'] = pd.to_numeric(chocolate_df.ReviewDate)
chocolate_df['CocoaPercent'] = pd.to_numeric(chocolate_df.CocoaPercent.str.replace('%','')) / 100
chocolate_df['Rating'] = pd.to_numeric(chocolate_df.Rating)

##### Plot ratings information #####
## Key stats
rating_mean = np.mean(chocolate_df.Rating)
rating_median = np.median(chocolate_df.Rating)
cocoa_percent_mean = np.mean(chocolate_df.CocoaPercent)
cocoa_percent_median = np.median(chocolate_df.CocoaPercent)

## Histogram of Ratings
plt.hist(chocolate_df.Rating, bins=16)
plt.title('Chocolate Tasting Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.axvline(rating_mean, c='r')
plt.axvline(rating_median, c='g')
plt.show()

## Highest Rated Chocolatier
## Calculate mean rating
chocolate_df_agg = chocolate_df.groupby('Company').Rating.mean().reset_index()

## Sort descending
chocolate_df_agg = chocolate_df_agg.sort_values(by='Rating', ascending=False).head(10)

## Bar Chart of Ratings
plt.figure(figsize=(20,8))
plt.bar(x=chocolate_df_agg.Company, height=chocolate_df_agg.Rating)
plt.title('Top 10 Chocolatiers by Rating')
plt.xlabel('Chocolatier')
plt.ylabel('Mean Rating')
plt.xticks(rotation=45, )
plt.axhline(rating_mean, c='r')
plt.axhline(rating_median, c='g')
plt.show()

## Clean up
del(chocolate_df_agg)

## Scatter plot of Rating ~ CocoaPercent
plt.scatter(x=chocolate_df.CocoaPercent, y=chocolate_df.Rating)
plt.title('Rating vs. Cocoa Percent')
plt.xlabel('Cocoa Percent')
plt.ylabel('Rating')
plt.axvline(cocoa_percent_mean, c = 'r')
plt.axvline(cocoa_percent_median, c = 'g')
plt.axhline(rating_mean, c='r')
plt.axhline(rating_median, c='g')
plt.show()

##### Fit line for Rating ~ CocoaPercent #####
x = chocolate_df.iloc[:, 4].values.reshape(-1, 1)
y = chocolate_df.iloc[:, 6].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)
y_prediction = linear_regressor.predict(x)

## Replot Scatter plot of Rating ~ CocoaPercent adding regression line
plt.scatter(x=chocolate_df.CocoaPercent, y=chocolate_df.Rating)
plt.plot(x, y_prediction, color='g')
plt.title('Rating vs. Cocoa Percent with Regression Line')
plt.xlabel('Cocoa Percent')
plt.ylabel('Rating')
plt.text(0.85,5, 'Coefficient: {0}'.format(round(linear_regressor.coef_[0][0],2)), {'color': 'C0', 'fontsize': 8})
plt.show()