#!/usr/bin/env python3
"""
Airport distance from the command line.

    python distance.py JFK LAX     # two airports
    python distance.py             # pick from popular routes

Reads APIVERVE_API_KEY from .env, like the web app.
"""
import sys

from apiverve import ApiError, call_api

ROUTES = [
    ('JFK', 'LAX', 'New York to Los Angeles'),
    ('LHR', 'JFK', 'London to New York'),
    ('SFO', 'NRT', 'San Francisco to Tokyo'),
    ('DXB', 'SIN', 'Dubai to Singapore'),
    ('SYD', 'LAX', 'Sydney to Los Angeles'),
]


def show_airport(label, a):
    where = ', '.join(p for p in (a.get('city'), a.get('state'), a.get('country')) if p)
    print(f"  {label:<5} {a['iata']}  {a['name']} ({where})")


def show(d):
    # Airports, heading and time zones are paid-plan fields; on the free plan they're empty.
    print()
    if d.get('airport1') and d.get('airport2'):
        show_airport('From', d['airport1'])
        show_airport('To', d['airport2'])
        print()
    print(f"  Distance     {d['distanceMiles']:,.0f} mi / {d['distanceKm']:,.0f} km")
    print(f"  Flight time  {d.get('estimatedFlightTime') or 'n/a'}")
    if d.get('direction'):
        print(f"  Heading      {d['direction']} ({d.get('bearing')}°)")
    if isinstance(d.get('timezoneDiffHours'), (int, float)):
        print(f"  Time zones   {d['timezoneDiffHours']:+} hours")
    print()


def pick_route():
    print('\nPopular routes:')
    for i, (a, b, name) in enumerate(ROUTES, 1):
        print(f'  {i}. {a} → {b}  {name}')
    choice = input('\nPick a route, or type two codes (e.g. CDG HND): ').strip().upper().split()
    if len(choice) == 1 and choice[0].isdigit() and 1 <= int(choice[0]) <= len(ROUTES):
        return ROUTES[int(choice[0]) - 1][:2]
    if len(choice) == 2:
        return choice
    raise SystemExit('Enter a route number, or two 3-letter airport codes.')


def main():
    origin, dest = sys.argv[1:3] if len(sys.argv) == 3 else pick_route()
    try:
        show(call_api('airportdistance', {'iata1': origin.upper(), 'iata2': dest.upper()}))
    except ApiError as err:
        raise SystemExit(f'Error: {err}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
