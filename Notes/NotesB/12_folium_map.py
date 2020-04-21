import folium
import csv

with open('Parks_-_Public_Art.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data.pop(0))
print(data[0])

lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]
names = [x[2] for x in data]

art_map = folium.Map(location=[41.880443, -87.644107], zoom_start=11, tiles='Stamen')

# FWP 41.923064, -87.638504
# Placing a marker
folium.Marker(location=(41.923064, -87.638504),
              popup='<b>{}</b>'.format("Francis W. Parker"),
              icon=folium.Icon(color='red', icon='graduation-cap', prefix='fa')  # Font-Awesome website
              ).add_to(art_map)

for i in range(len(data)):
    folium.Marker(location=(lats[i], longs[i]),
                  popup=names[i],
                  icon=folium.Icon(color='blue', icon='paint-brush', prefix='fa')
                  ).add_to(art_map)


art_map.save('art_map.html')

