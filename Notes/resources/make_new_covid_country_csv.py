"""
Example of dot density map
"""

import csv
import requests

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
response = requests.get(url)

with open('covid_county.csv', 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))
