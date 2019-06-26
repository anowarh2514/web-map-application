import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'red'
    elif 1000<= elevation <1500:
        return 'green'
    elif 1500<= elevation <2000:
        return 'lightblue'
    elif 2000<= elevation <2500:
        return 'orange'
    elif 2500<= elevation <3000:
        return 'purple'
    else:
        return 'darkblue'

map = folium.Map(location = [38.58,-99.09],zoom_start = 6, tiles = "Mapbox Bright")
fgv = folium.FeatureGroup(name = "Location Wise")

for lt,ln,nm,el in zip(lat,lon,name,elev):
  fgv.add_child(folium.Marker(location = [lt,ln],radius = 6 , popup = nm + " - " + str(el)+"m",icon = folium.Icon(color = color_producer(el)),color = 'gray' ,fill_opacity = 0.7))
fgp = folium.FeatureGroup(name = "Population Wise")
fgp.add_child(folium.GeoJson(data = open('world.json','r',encoding = 'utf-8-sig').read(),
                            style_function = lambda x: { 'fillColor':'red' if x['properties']['POP2005']<8000000
                            else 'darkblue' if 8000000 <= x['properties']['POP2005']<10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005']<15000000
                            else 'yellow' if 15000000 <= x['properties']['POP2005']<20000000 else 'green'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")