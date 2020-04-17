
# There was some difficulty scraping a tweet.
# After a closer look, you can't do it from the dynamic webpage any longer
# I will give you some separate code to show you how to scrape a dynamic page.
# Feel free to skip if you don't want to try it.  (no penalty)

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


'''
I inspected a tweet and saw this span tag...

<span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">’s voice is one that can do that. Jennifer: Thank you for calming our spirits through your song, “Moan.” Watch my free </span>
'''

oprah_url = "https://twitter.com/oprah?lang=en"

page = requests.get(oprah_url)
print(page)  # 200 is a good request
# print(page.text)  # text of the webpage (not that useful)


soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())  # make it print formatted


tweets = soup.find_all('span', class_="css-901oao")

print(tweets)


