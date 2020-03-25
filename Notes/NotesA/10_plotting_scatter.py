import csv
import matplotlib.pyplot as plt

with open("World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)


header = data.pop(0)
print(header)

# make a scatter of firearms_per_100 vs homicides_per_100k

homicide_100k = []
firearms_100 = []
names = []

for country in data:
    try:
        homicides = float(country[5])
        firearms = float(country[-2])
        name = country[0]
        homicide_100k.append(homicides)
        firearms_100.append(firearms)
        names.append(name)
    except:
        print(country[0], "invalid data")


print(names)

plt.figure