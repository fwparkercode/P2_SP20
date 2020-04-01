'''
Reading a csv from a url
(Comma Separated Values from Uniform Resource Locator)

scatter plot with colors and sizes
'''
import csv
import requests
import matplotlib.pyplot as plt

def get_data(url):
    with requests.Session() as s:
        download = s.get(url)
        download = download.content.decode('utf-8')
        reader = csv.reader(download.splitlines(), delimiter=",")
        data = list(reader)
    return data


url = "https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD"
data = get_data(url)
header = data.pop(0)

print(header)

ghg_index = header.index("Total GHG Emissions (Metric Tons CO2e)")
sqft_index = header.index("Gross Floor Area - Buildings (sq ft)")
type_index = header.index("Primary Property Type")

print(data[:10])
print(len(data))

valid_data = []

for building in data:
    try:
        float(building[ghg_index])
        float(building[sqft_index])
        if building[type_index] == "K-12 School" and building[0] == "2018":
            valid_data.append(building)
    except:
        pass

print(len(valid_data))

valid_data.sort(key=lambda x: float(x[ghg_index + 1]))

ghg = [float(x[ghg_index]) for x in valid_data]
sqft = [float(x[sqft_index]) for x in valid_data]

colors = ["green" for x in valid_data]
for i in range(37):
    colors[i] = "red"


plt.figure("GHG School Plot")

plt.scatter(ghg, sqft, alpha=0.3, c=colors)  # s for size and c for color (arrays)

plt.show()