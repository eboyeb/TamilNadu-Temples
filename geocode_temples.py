import json
import requests
import time

def geocode(address):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address + ", Tamil Nadu, India",
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "tamilnadutemplesmap/1.0 (elaiyabharathi.c@gmail.com)"
    }
    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code == 200:
        results = response.json()
        if results:
            return float(results[0]["lat"]), float(results[0]["lon"])
        else:
            print(f"No results found for {address}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
    return None

# Load the temples data
with open('temples.json', 'r', encoding='utf-8') as f:
    temples = json.load(f)

# Geocode each temple
for temple in temples:
    if "coordinates" not in temple:
        coords = geocode(temple["location"])
        if coords:
            temple["coordinates"] = coords
        time.sleep(1)  # Be nice to the API

# Save the updated data
with open('temples_geocoded.json', 'w', encoding='utf-8') as f:
    json.dump(temples, f, ensure_ascii=False, indent=4)

print("Geocoding completed and saved to temples_geocoded.json")