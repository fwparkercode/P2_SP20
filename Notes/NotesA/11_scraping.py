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

# by attribute
print("\n" * 5)
big_font = soup.find_all(style="font-size: 8px")  # find_all returns all in a "list"
print(big_font)
print(big_font[0].text)  # iterable, can index, and has attributes

print(type(big_font))
print(type(big_font[0]))

# by css class
print("\n" * 5)
quote_divs = soup.find_all(class_="quote")
print(quote_divs[0].find("span").text)  # use find on bs4 ResultSet
print(quote_divs[0].span)  # use dot notation to drill down

quote_list = []
for quote in quote_divs:
    quote_list.append(quote.span.text)

quote_list = [x.span.text for x in quote_divs]

print(quote_list)


# combine attributes and tags
# find authors
author_tags = soup.find_all("small", class_="author",itemprop="author")
author_list = [x.text for x in author_tags]
print(author_list)

print(len(author_list), len(quote_list))

# print back the quotes
for i in range(len(author_list)):
    print(quote_list[i])
    print("\t\t--- {}".format(author_list[i]))
    print()

# target attributes
first_author_tag = author_tags[0]
print(first_author_tag)
print(first_author_tag['itemprop'])