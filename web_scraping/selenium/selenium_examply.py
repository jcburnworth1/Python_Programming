## Import libraries
from selenium import webdriver

## Setup browser
browser = webdriver.Chrome()

## Go to URL
browser.get('https://automatetheboringstuff.com/')

## Capture that element
elem = browser.find_element_by_css_selector('body > div.main > ul:nth-child(16) > li:nth-child(1) > a')

elem = browser.find_element_by_xpath(xpath='/html/body/div[2]/ul[2]/li[1]/a')

## Click the link
elem.click()

