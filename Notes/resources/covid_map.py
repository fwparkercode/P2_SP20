"""
Example of dot density map
"""
from geoplotlib.utils import read_csv
import requests
import csv
import pandas as pd


country_df = pd.read_csv("Geocodes_USA_with_Counties.csv")
country_df.head()

#
# with open("Geocodes_USA_with_Counties.csv") as f:
#     reader = csv.reader(f)
#     county_geo = list(reader)
#
# county_header = county_geo.pop(0)
# print(county_header)
#
# county_loc = "covid_county.csv"
# with open(county_loc) as f:
#     reader = csv.reader(f)
#     covid_county = list(reader)
#
# covid_header = covid_county.pop(0)
# print(covid_header)
#
#
#
# geo = "all-geocodes-v2017.csv"
# with open(geo) as f:
#     reader = csv.reader(f)
#     geocodes = list(reader)
#
# geo_header = geocodes.pop(0)
# print(geo_header)
#
#
# # data = read_csv(county_url)
# # geoplotlib.dot(data)
# # geoplotlib.show()