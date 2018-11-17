import json
import urllib.request
import sys
from collections import namedtuple

if __name__ == "__main__":
    # pobrać id dla lkalizacji
    location_id = get_location_id(sys.argv[1])
    print(location_id)
    # ponrac pogode dla lokalizacji
    # wyswietlic wynik






with urllib.request.urlopen("https://www.metaweather.com/api/location/search/?query={location_name }") as f:
    print(f)
    pogoda = json.loads(f.read())

title = pogoda[0]['title']
for c in title:
    print(f"{r['location_type']} - {r['woeid']}")

#### uruchom z linii komend
# jako apka
