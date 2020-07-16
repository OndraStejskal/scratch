from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import json
import folium
import re

CZ_COORDINATES = (49.80000000038, 15.470899668649)

if __name__ == "__main__":

    page_url = "https://www.evmapa.cz/"

    uCLient = uReq(page_url)

    # creating soup object
    page_soup = soup(uCLient.read(), "html.parser")
    #uCLient.close
    markers = page_soup.findAll('script')[2]
    string_markers = str(markers)

    # using regex to get array of coordinates
    x = re.search("\[(.+?)\]", string_markers)
    if x:
        raw_string = x.group(1)
    raw_array = re.split(",", raw_string)

    # creating map of charging stations
    map = folium.Map(location=CZ_COORDINATES)
    data = []
    for i in range(1): #range(int(len(raw_array) / 4)):
        j = 4 * i

        coords = (raw_array[j + 1], raw_array[j + 2])
        folium.Marker(coords, popup=raw_array[j]).add_to(map)
        data.append({'lat': raw_array[j + 1], 'lng': raw_array[j + 2]})
    map.save('ev_map.html')
    print(data)



