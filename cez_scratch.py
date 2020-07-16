from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import json
import folium

CZ_COORDINATES = (49.80000000038, 15.470899668649)



page_url = "https://www.elektromobilita.cz/cs/mapa-dobijecich-stanic"

uCLient = uReq(page_url)

page_soup = soup(uCLient.read(), "html.parser")
uCLient.close

markers = page_soup.body.main.section['data-markers']
data = json.loads(markers)

map = folium.Map(location=CZ_COORDINATES)

k = 0;
for item in data:
    coords = (item['lat'], item['lng'])
    folium.Marker(coords, popup=item['lat']).add_to(map)
    k += 1

print(k)
map.save('index.html')
print('wakaflocka')