import folium
import csv

with open('Parks_-_Public_Art.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

# 41.8781° N, 87.6298° W
m = folium.Map(location=[41.8781, -87.6298], zoom_start=11)

print(data.pop(0))


lats = [float(y[-3]) for y in data]
longs = [float(x[-2]) for x in data]
names = [x[2] for x in data]

for i in range(len(lats)):
    folium.Marker(
        location=[lats[i], longs[i]],
        popup=names[i],
        icon=folium.Icon(icon='smile-o', prefix='fa', color='blue')
    ).add_to(m)


m.save('mymap.html')

print(help(folium.Icon))

