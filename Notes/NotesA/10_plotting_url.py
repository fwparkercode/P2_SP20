"""
Reading a csv from a url
Comma Separated Values from a Uniform Resource Locator

scatter plot sizes and color
"""
import csv
import requests
import matplotlib.pyplot as plt

def get_data(url):
    with requests.Session() as s:
        download = s.get(url)
        content = download.content.decode('utf-8')
        reader = csv.reader(content.splitlines(), delimiter=',')
        my_list = list(reader)
    return my_list


data = get_data("https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD")
header = data.pop(0)

print(header)

ghg_index = header.index("Total GHG Emissions (Metric Tons CO2e)")
sqft_index = header.index("Gross Floor Area - Buildings (sq ft)")
type_index = header.index("Primary Property Type")


valid_data = []
print(len(data))

for building in data:
    try:
        int(building[ghg_index])
        int(building[sqft_index])
        if building[type_index] == "K-12 School":
            valid_data.append(building)
    except:
        pass

print(len(valid_data))

ghg = [int(x[ghg_index]) for x in valid_data]
color = []
for building in ghg:
    if building > 4000:
        color.append("red")
    else:
        color.append("green")


sqft = [int(x[sqft_index]) for x in valid_data]



plt.figure(1, tight_layout=True)

plt.scatter(sqft, ghg, alpha=0.3, c=color)  # s for size, c for color (arrays
plt.legend()

plt.show()
