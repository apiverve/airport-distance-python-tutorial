# Airport Distance Calculator | APIVerve Template

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB)](requirements.txt) [![Flask](https://img.shields.io/badge/Flask-3-000000)](app.py)
[![APIVerve | Airport Distance](https://img.shields.io/badge/APIVerve-Airport_Distance-purple)](https://apiverve.com/marketplace/airportdistance?utm_source=github&utm_medium=template&utm_campaign=airport-distance-python-tutorial)

The distance and flight time between any two airports, from their 3-letter codes. A web app you can deploy, and a command-line tool.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fapiverve%2Fairport-distance-python-tutorial&project-name=airport-distance&repository-name=airport-distance&env=APIVERVE_API_KEY&envDescription=Your%20APIVerve%20API%20key.%20Free%20to%20create%2C%20no%20card%20needed.&envLink=https%3A%2F%2Fdashboard.apiverve.com%2Fsignup%3Fapi%3Dairportdistance%26utm_source%3Dvercel%26utm_medium%3Dtemplate%26utm_campaign%3Dairport-distance-python-tutorial)

![Airport Distance Calculator showing JFK to LAX](https://raw.githubusercontent.com/apiverve/airport-distance-python-tutorial/main/screenshot.png)

---

### Get your free API key

This template needs an APIVerve API key. **[Sign up free](https://dashboard.apiverve.com/signup?api=airportdistance&utm_source=github&utm_medium=template&utm_campaign=airport-distance-python-tutorial)**, no credit card required.

---

## Deploy in one click

Click **Deploy with Vercel** above. Vercel copies this repo to your GitHub account, asks for your `APIVERVE_API_KEY`, and gives you a live URL about a minute later.

## Run it locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/apiverve/airport-distance-python-tutorial.git
   cd airport-distance-python-tutorial
   ```

2. **Install the dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Add your API key**
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and set `APIVERVE_API_KEY`.

4. **Start it**
   ```bash
   python app.py
   ```

5. **Open** `http://localhost:3000`

`python app.py` serves the page and the API route together, so you don't need the Vercel CLI.

## Use it from the command line

```bash
python distance.py JFK LAX
```

Run it with no arguments to be prompted instead. It reads the same `.env` as the web app.

## How it works

1. The page (`public/index.html`) calls `GET /api/distance?from=JFK&to=LAX`.
2. `app.py` checks both codes are 3 letters, then calls Airport Distance. Your API key stays on the server and never reaches the browser.
3. The page shows the result.

```
├── app.py             # Flask app: the /api/distance route, which holds your key
├── apiverve.py        # Shared by app.py and distance.py: the key, the APIVerve call, the rate limit
├── distance.py        # The command-line version
├── public/            # The page: index.html, app.js, ui.js, style.css
├── requirements.txt   # flask, requests
├── .python-version    # 3.12, for Vercel
└── .env.example       # Copy to .env and add your key
```

### The API call

```python
res = requests.get(
    'https://api.apiverve.com/v1/airportdistance',
    params={'iata1': 'JFK', 'iata2': 'LAX'},
    headers={'x-api-key': os.environ['APIVERVE_API_KEY']},
)
data = res.json()['data']
# data['distanceMiles'], data['distanceKm'], data['estimatedFlightTime']
```

Some response fields are for paid plans and come back empty on the free plan. The page shows whatever it gets and leaves the rest out, so it works on every plan.

## Before you share your URL

Once deployed, anyone who finds your URL can use it on your API key. Each visitor can make 10 requests a minute, which is fine for a demo. The limit is kept in memory, so it isn't shared between serverless instances. For production:

- Put the page behind your own sign-in, or
- Move the limit to a shared store such as [Upstash Redis](https://upstash.com/), or
- Call the route only from your own backend.

## Ideas to extend it

- Show the distance on a flight search or booking page
- Estimate travel emissions for trip reports
- Look up the airports themselves with [Airports Lookup](https://apiverve.com/marketplace/airports?utm_source=github&utm_medium=template&utm_campaign=airport-distance-python-tutorial)

## API reference

- [Airport Distance](https://apiverve.com/marketplace/airportdistance?utm_source=github&utm_medium=template&utm_campaign=airport-distance-python-tutorial): `GET https://api.apiverve.com/v1/airportdistance?iata1=&iata2=`
- [Full documentation](https://docs.apiverve.com?utm_source=github&utm_medium=template&utm_campaign=airport-distance-python-tutorial)

## Tech stack

- **Flask** for the API route, with **requests** to call APIVerve (Python 3.12)
- Plain HTML, CSS and JavaScript for the page: no framework and no build step
- Deploys to Vercel as-is: `app.py` becomes a Python function and `public/` is served from the CDN

## License

MIT. See [LICENSE](LICENSE).
