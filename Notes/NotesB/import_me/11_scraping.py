# Web scraping

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"  # uniform resource locator

page = requests.get(url)
print(page)  # prints the response

# print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())  # nicer way to look at it

# find data by tagname
# find method just gets the first one it finds
title = soup.find("title")  # title is the tag name
print(title)
print(title.text)

# by attribute
print("\n" * 10)
authors = soup.find_all(itemprop="author")
print(authors)
print(type(authors))

for author in authors:
    print(author.text)

# by css class
print("\n" * 10)
quotes = soup.find_all(class_="quote")
print(quotes[0].prettify())

# drill down using dot notation
print(quotes[0].span)
print(quotes[0].span.text)

for quote in quotes:
    print(quote.span.text)


# use authors and quotes together
for i in range(len(quotes)):
    print(quotes[i].span.text)
    print("\t\t---{}".format(authors[i].text))
    print()


# You can also combine search terms

quotes = soup.find_all("span", class_="text", itemprop="text")

for quote in quotes:
    print(quote.text)







