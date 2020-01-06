## Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

## Get the page from the net & store the content
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content

print(webpage_response)
print(webpage)

## Setup a BeautifulSoup object to parse the webpage
soup = BeautifulSoup(webpage, 'html.parser')

print(soup)

## Print out first paragraph
print(soup.p)
print(soup.p.string)

## Looping over children in the tree
for child in soup.div.children:
    print(child)

## Find all div
print(soup.find_all('div'))

## Find turtle links
turtle_links = soup.find_all('a')
print(turtle_links)

## Getting the links to other pages
prefix = 'https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/'

## Capture the links
links = []

## Go through all of the a tags and get the links associated with them:
for a in turtle_links:
    # print(a)
    links.append(prefix + a["href"])

## Define turtle_data
turtle_data = {}

## Follow each link:
for link in links:
    webpage = requests.get(link)
    turtle = BeautifulSoup(webpage.content, "html.parser")
    turtle_name = turtle.select(".name")[0].get_text()

    stats = turtle.find("ul")
    stats_text = stats.get_text()
    turtle_data[turtle_name] = stats_text.split("\n")
    ## Clean out empty list elements
    turtle_data[turtle_name] = turtle_data[turtle_name][1:6]

print(turtle_data)

## Clean up
del(a, child, link, links, prefix, soup, stats, stats_text, turtle,
    turtle_links, turtle_name, webpage, webpage_response)

## Convert turtle_data to dataframe
turtle_data_df = pd.DataFrame.from_dict(turtle_data, orient='index')
turtle_data_df.insert(loc=0, column='Name', value=turtle_data_df.index)

## Clean column names
columns = ['name', 'age', 'weight', 'sex', 'breed', 'source']

turtle_data_df.columns = columns

## Clean up
del(columns, turtle_data)

## Clean the columns
## Age
turtle_data_df['age'] = pd.to_numeric(turtle_data_df.age.str.split(':', expand=True)[1].str.replace(' Years? Old',''))

## Weight
turtle_data_df['weight'] = pd.to_numeric(turtle_data_df.weight.str.split(':', expand=True)[1].str.replace(' lbs?',''))

## Sex
turtle_data_df['sex'] = turtle_data_df.sex.str.split(': ', expand=True)[1]

## Breed
turtle_data_df['breed'] = turtle_data_df.breed.str.split(': ', expand=True)[1]

## Source
turtle_data_df['source'] = turtle_data_df.source.str.split(': ', expand=True)[1].str.title()
