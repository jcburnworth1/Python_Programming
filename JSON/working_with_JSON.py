## Import libraries
import os
import requests
import pandas as pd
from pandas.io.json import json_normalize

## Variables
api_key = os.environ['api_key']
api_url = 'https://api.yelp.com/v3/businesses/search'
params = {'location': 'NYC', 'sort_by': 'rating', 'term': 'cafe'}
headers = {'Authorization': "Bearer {}".format(api_key)}

## Query the Yelp API with headers and params set
response = requests.get(api_url, headers=headers, params=params)

## Extract JSON data from response
data = response.json()

## Load "businesses" values to a data frame and print names
cafes = pd.DataFrame(data['businesses']) # This work but does not handle the nested data - See below for that
print(cafes.name)

## Formatting the nested JSON
cafes_2 = json_normalize(data['businesses'], sep='_') # Handles basic nested data

## Flatten all the data
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=['name',
                                  'alias',
                                  'rating',
                          		  ['coordinates', 'latitude'],
                          		  ['coordinates', 'longitude']],
                    		meta_prefix='biz_')



# View the data
print(flat_cafes.head())