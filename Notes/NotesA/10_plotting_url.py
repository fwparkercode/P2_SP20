"""
Reading a csv from a url
Comma Separated Values from a Uniform Resource Locator

scatter plot sizes and color
"""
import csv
import requests

url = "https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD"

with requests.Session() as s:
    download = s.get(url)
    content = download.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    my_list = list(reader)

print(my_list)