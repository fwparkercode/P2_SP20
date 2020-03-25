import csv
import matplotlib.pyplot as plt
import numpy as np

with open("World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

header = data.pop(0)
print(header)

# make a scatter of firearms_per_100 vs homicides_100k

homicide_100k = []
firearms_100 = []
countries = []
similar = ["Canada", "England and Wales", "Japan", "South Korea", "France", "Germany", "Switzerland", "Ireland", "China", "Singapore", "Hungary", "Israel", "Taiwan", "Iceland", "Spain", "Belgium", "Finland", "Netherlands", "United States"]

data = [x for x in data if x[0] in similar]


for country in data:
    try:
        homicides = float(country[5])
        firearms = float(country[-2])
        name = country[0]
        homicide_100k.append(homicides)
        firearms_100.append(firearms)
        countries.append(name)
    except:
        print(country[0], "data is inadequate.")

print(countries)

plt.figure("Homicides per Firearm Worldwide", figsize=(10, 6))  # add figsize

plt.scatter(firearms_100, homicide_100k)
plt.ylabel("homicides per 100k population")
plt.xlabel("firearms per 100 people")
plt.title("Homicides vs. Gun Ownership by Country")


plt.annotate("MY TEXT", xy=(50, 50))

for i in range(len(countries)):
    plt.annotate(countries[i], xy=(firearms_100[i], homicide_100k[i]))



plt.show()
