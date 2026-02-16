#!/usr/bin/env python3
"""
Airport Distance Calculator - APIVerve API Tutorial
Calculate the distance between any two airports using IATA codes.
"""

import os
import requests

API_KEY = os.environ.get('APIVERVE_API_KEY', 'your-api-key-here')
API_URL = 'https://api.apiverve.com/v1/airportdistance'


def get_airport_distance(airport1, airport2):
    """Get distance between two airports by IATA code."""
    headers = {
        'x-api-key': API_KEY
    }

    params = {
        'airport1': airport1.upper(),
        'airport2': airport2.upper()
    }

    response = requests.get(API_URL, headers=headers, params=params)
    return response.json()


def display_airport_info(airport, label):
    """Display formatted airport information."""
    print(f"\n  {label}:")
    print(f"    Name:      {airport['name']}")
    print(f"    IATA/ICAO: {airport['iata']} / {airport['icao']}")
    print(f"    Location:  {airport['city']}, {airport['state']}, {airport['country']}")
    print(f"    Elevation: {airport['elevation']:,} ft")
    print(f"    Coords:    {airport['latitude']:.4f}, {airport['longitude']:.4f}")


def display_result(data):
    """Display distance calculation results."""
    if data.get('status') != 'ok':
        print(f"\nError: {data.get('error', 'Unknown error')}")
        return

    result = data['data']

    print("\n" + "=" * 60)
    print("           AIRPORT DISTANCE CALCULATOR")
    print("=" * 60)

    display_airport_info(result['airport1'], "From")
    display_airport_info(result['airport2'], "To")

    print("\n" + "-" * 60)
    print(f"\n  DISTANCE:")
    print(f"    {result['distanceMiles']:,.2f} miles")
    print(f"    {result['distanceKm']:,.2f} kilometers")

    # Calculate approximate flight time (assuming 500 mph average)
    flight_hours = result['distanceMiles'] / 500
    hours = int(flight_hours)
    minutes = int((flight_hours - hours) * 60)
    print(f"\n  Estimated Flight Time: ~{hours}h {minutes}m")

    print("\n" + "=" * 60)


def main():
    """Main function with popular route examples."""
    print("\nAirport Distance Calculator")
    print("===========================")

    # Popular routes
    routes = [
        ("JFK", "LAX", "New York to Los Angeles"),
        ("LHR", "JFK", "London to New York"),
        ("SFO", "NRT", "San Francisco to Tokyo"),
        ("DXB", "SIN", "Dubai to Singapore"),
        ("SYD", "LAX", "Sydney to Los Angeles"),
    ]

    print("\nPopular routes:")
    for i, (a1, a2, desc) in enumerate(routes, 1):
        print(f"  {i}. {a1} → {a2} ({desc})")
    print("  6. Enter custom airports")

    try:
        choice = input("\nSelect option (1-6): ").strip()

        if choice == '6':
            airport1 = input("Enter first airport IATA code (e.g., JFK): ").strip()
            airport2 = input("Enter second airport IATA code (e.g., LAX): ").strip()
        elif choice in ['1', '2', '3', '4', '5']:
            airport1, airport2, _ = routes[int(choice) - 1]
        else:
            print("Invalid choice. Using JFK to LAX.")
            airport1, airport2 = 'JFK', 'LAX'

        if len(airport1) != 3 or len(airport2) != 3:
            print("\nIATA codes must be 3 letters (e.g., JFK, LAX, LHR)")
            return

        print(f"\nCalculating distance from {airport1.upper()} to {airport2.upper()}...")
        result = get_airport_distance(airport1, airport2)
        display_result(result)

    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except requests.RequestException as e:
        print(f"\nAPI request failed: {e}")


if __name__ == '__main__':
    main()
