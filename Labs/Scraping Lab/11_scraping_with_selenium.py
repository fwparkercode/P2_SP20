# Web Scraping with Beautiful Soup
import time
import urllib.request
import certifi
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


# BELOW IS SOME CODE I WROTE FOR DYNAMIC WEBSITE SCRAPING
# I am scraping Oprah's account like in class
# I will let you do twitter, I will attempt instagram.
# I am using a library called selenium which performs much like a browser.
# It uses an extension called "chromedriver" to open chrome.
# You would need the most recent version of Chrome to get this code to work
# also, you will need to change the path info for chromedriver.  Use your own path
# (just copy path with right click from project tab (file menu))

#launch url
twit_url = "https://twitter.com/oprah?lang=en"
instagram_url = "https://www.instagram.com/oprah/"


# create a new chrome session
# need to have chromedriver executable in project for this.  It can be downloaded and installed.  You can even download the driver and dump it directly into the folder for this project.  That's what I will do here.

# YOU MIGHT NEED TO CHANGE THIS TO THE FULL PATH!!  Just left click the file.
# ex: /Users/alee/PycharmProjects/P2_SP20/Notes/NotesA/chromedriver for my computer
driver = webdriver.Chrome("/Users/alee/PycharmProjects/P2_SP20/Labs/Scraping Lab/chromedriver")  #in same folder, chromedriver


driver.implicitly_wait(10)  # wait 10 sec to load page so the html builds
driver.get(instagram_url)  # this gets the web page after it loads


# Get scroll height
# This will help you with scraping twitter.  You can scroll down!
last_height = driver.execute_script("return document.body.scrollHeight")  # this is so I can scroll down and grab more stuff


x = 0
pages_to_scroll = 20

while x < pages_to_scroll:
    # Scroll down to bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    x += 1

    # Wait to load page
    time.sleep(1)  # seconds to let it load the new posts

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # reached the bottom or maybe didn't load
    last_height = new_height # reset for next loop iteration

#################################
# Now that full page has loaded #
#################################
# use lxml here, html.parser might not be lenient enough for this site
soup = BeautifulSoup(driver.page_source, 'lxml')  # lxml is a better parser.  Might need to install it from preferences.
print(soup.prettify())


pics = soup.findAll("img", class_="FFVAD") # image tags with a class
links = [x.get("src") for x in pics] # grab src attribute from img

# At first I got a certificate authentication error.
# I ran the following two files to install cert.
# this seems to be a python 3.6 or greater thing
# Install Certificates.command
# Update Shell Profile.command
# worked immediately for me after doing this


# code below grabs all the instagram pics from the page.
# if you add some code to press the "See More" button, you could grab more.  (Spoiler: you sure can!)
# this would work for Twitter as well
for i in range(len(links)):
    urllib.request.urlretrieve(links[i], '../oprah_instagram_pics/pic' + str(i) + ".jpg")



