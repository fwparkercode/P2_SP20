import folium
import csv


with open('Parks_-_Public_Art.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

art_map = folium.Map(location=[41.8781, -87.6298], zoom_start=11)

print(data.pop(0))

# Parker 41.923000, -87.638461
# placing a marker on the map
folium.Marker(location=[41.923000, -87.638461],
              popup="Our School",
              icon=folium.Icon(color='red', icon='graduation-cap', prefix='fa'),
              ).add_to(art_map)

lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]
names = [x[2] for x in data]

for i in range(len(data)):
    folium.Marker(location=[lats[i], longs[i]],
                  popup='<span><b>{}</b></span>'.format(names[i]),
                  icon=folium.Icon(color='orange', icon='paint-brush', prefix='fa')
                  ).add_to(art_map)


art_map.save('my_artmap.html')

help(folium.Marker)