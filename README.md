# Airport Distance Calculator | APIVerve API Tutorial

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab)](https://python.org)
[![APIVerve | Airport Distance](https://img.shields.io/badge/APIVerve-Airport_Distance-purple)](https://apiverve.com/marketplace/airportdistance?utm_source=github&utm_medium=tutorial&utm_campaign=airport-distance-python-tutorial)

A Python CLI tool to calculate the distance between any two airports. Enter IATA codes and get the distance in miles and kilometers, plus detailed airport information.

![Screenshot](https://raw.githubusercontent.com/apiverve/airport-distance-python-tutorial/main/screenshot.jpg)

---

### Get Your Free API Key

This tutorial requires an APIVerve API key. **[Sign up free](https://dashboard.apiverve.com?utm_source=github&utm_medium=tutorial&utm_campaign=airport-distance-python-tutorial)** - no credit card required.

---

## Features

- Calculate distance between any two airports
- Distance in miles and kilometers
- Detailed airport information
- IATA and ICAO codes
- City, state, country data
- Elevation and coordinates
- Estimated flight time
- Popular route presets

## Quick Start

1. **Clone this repository**
   ```bash
   git clone https://github.com/apiverve/airport-distance-python-tutorial.git
   cd airport-distance-python-tutorial
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key**
   ```bash
   export APIVERVE_API_KEY=your-api-key-here
   ```

4. **Run the calculator**
   ```bash
   python distance.py
   ```

## Project Structure

```
airport-distance-python-tutorial/
├── distance.py         # Main Python script
├── requirements.txt    # Python dependencies
├── screenshot.jpg      # Preview image
├── LICENSE             # MIT license
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## How It Works

1. Enter two IATA airport codes
2. API looks up both airports
3. Calculates great-circle distance
4. Returns full airport details

### The API Call

```python
response = requests.get('https://api.apiverve.com/v1/airportdistance',
    headers={'x-api-key': API_KEY},
    params={
        'airport1': 'JFK',
        'airport2': 'LAX'
    }
)
```

## API Reference

**Endpoint:** `GET https://api.apiverve.com/v1/airportdistance`

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `airport1` | string | Yes | First airport IATA code |
| `airport2` | string | Yes | Second airport IATA code |

**Example Response:**

```json
{
  "status": "ok",
  "error": null,
  "data": {
    "distanceMiles": 2470.23,
    "distanceKm": 3974.2,
    "airport1": {
      "name": "John F Kennedy International Airport",
      "iata": "JFK",
      "icao": "KJFK",
      "city": "New York",
      "state": "New-York",
      "country": "US",
      "elevation": 13,
      "latitude": 40.63980103,
      "longitude": -73.77890015
    },
    "airport2": {
      "name": "Los Angeles International Airport",
      "iata": "LAX",
      "icao": "KLAX",
      "city": "Los Angeles",
      "state": "California",
      "country": "US",
      "elevation": 125,
      "latitude": 33.94250107,
      "longitude": -118.4079971
    }
  }
}
```

## Airport Data Fields

| Field | Description |
|-------|-------------|
| `name` | Full airport name |
| `iata` | 3-letter IATA code |
| `icao` | 4-letter ICAO code |
| `city` | City name |
| `state` | State/province/region |
| `country` | Country code |
| `elevation` | Elevation in feet |
| `latitude` | Latitude coordinate |
| `longitude` | Longitude coordinate |

## Popular Routes

| Route | Distance |
|-------|----------|
| JFK → LAX | 2,470 miles |
| LHR → JFK | 3,451 miles |
| SFO → NRT | 5,130 miles |
| DXB → SIN | 3,637 miles |
| SYD → LAX | 7,488 miles |

## Common IATA Codes

| Code | Airport |
|------|---------|
| JFK | New York JFK |
| LAX | Los Angeles |
| LHR | London Heathrow |
| CDG | Paris Charles de Gaulle |
| NRT | Tokyo Narita |
| DXB | Dubai |
| SIN | Singapore Changi |
| SYD | Sydney |
| ORD | Chicago O'Hare |
| ATL | Atlanta |

## Customization Ideas

- Add route visualization on map
- Calculate carbon emissions
- Compare multiple routes
- Find nearest airports
- Build flight search
- Add layover calculations

## Related APIs

Explore more APIs at [APIVerve](https://apiverve.com/marketplace?utm_source=github&utm_medium=tutorial&utm_campaign=airport-distance-python-tutorial):

- [Airports Lookup](https://apiverve.com/marketplace/airportslookup?utm_source=github&utm_medium=tutorial&utm_campaign=airport-distance-python-tutorial) - Search airports
- [Airline Lookup](https://apiverve.com/marketplace/airlinelookup?utm_source=github&utm_medium=tutorial&utm_campaign=airport-distance-python-tutorial) - Airline information
- [Distance Calculator](https://apiverve.com/marketplace/distancecalculator?utm_source=github&utm_medium=tutorial&utm_campaign=airport-distance-python-tutorial) - General distance calc

## License

MIT - see [LICENSE](LICENSE)

## Links

- [Get API Key](https://dashboard.apiverve.com?utm_source=github&utm_medium=tutorial&utm_campaign=airport-distance-python-tutorial) - Sign up free
- [APIVerve Marketplace](https://apiverve.com/marketplace?utm_source=github&utm_medium=tutorial&utm_campaign=airport-distance-python-tutorial) - Browse 300+ APIs
- [Airport Distance API](https://apiverve.com/marketplace/airportdistance?utm_source=github&utm_medium=tutorial&utm_campaign=airport-distance-python-tutorial) - API details
