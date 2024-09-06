import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_Hindu_temples_in_Tamil_Nadu"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

temples = []

# Find all tables with class 'wikitable'
tables = soup.find_all('table', class_='wikitable')

for table in tables:
    rows = table.find_all('tr')[1:]  # Skip the header row
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 2:
            temple_name = cols[0].text.strip()
            location = cols[1].text.strip()
            temples.append({
                "name": temple_name,
                "location": location
            })

# Save the data to a JSON file
with open('temples.json', 'w', encoding='utf-8') as f:
    json.dump(temples, f, ensure_ascii=False, indent=4)

print(f"Scraped {len(temples)} temples and saved to temples.json")