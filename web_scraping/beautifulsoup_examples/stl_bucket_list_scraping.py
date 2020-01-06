## Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

## Get the page from the net & store the content
webpage_response = requests.get('https://bucketlistjourney.net/st-louis-bucket-list-things-to-do/?fbclid=IwAR3aRgXDwJddtASc8uwuJFMZZjg8ZZuoDjJ1OnPCnUwHC44ANlgJVt0unmo')
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
print(soup.find_all('h3'))