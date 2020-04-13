# Scraping with Beautiful Soup

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"  # uniform resource locator

page = requests.get(url)
print(page)  # 200 is a good request
# print(page.text)  # text of the webpage (not that useful)


soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())  # make it print formatted

# find data in our soup object
# by tagname
title = soup.find("title")  # look for the <title> and returns the first one

print(title)