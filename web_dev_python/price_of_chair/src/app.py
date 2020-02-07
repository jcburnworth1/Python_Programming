## Load Libraries
import requests
from bs4 import BeautifulSoup

def get_chair_webpage():
    ## Initial request
    request = requests.get("https://www.johnlewis.com/john-lewis-partners-reid-faux-leather-office-chair/black/p3176358")
    content = request.content

    return content

def get_chair_price():
    ## Parse and find the price data
    content = get_chair_webpage()
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find("p", {"class": "price price--large"})
    price_text = element.text.strip()[1:]
    price_float = float(price_text)

    return price_float

## Run program
if __name__ == '__main__':
    price = get_chair_price()

    print("Price of Chair is: ${}".format(price))