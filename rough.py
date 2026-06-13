import requests
from datetime import datetime, timedelta
from pprint import pprint

# ==================== SERP API ====================

SERP_API_KEY = "YOUR_SERP_API_KEY"
SERP_API_ENDPOINT = "https://serpapi.com/search"

# ==================== DATE ====================

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

# ==================== USER INPUT ====================

departure_destination = input("Enter the departure airport code: ").upper()
arrival_destination = input("Enter the arrival airport code: ").upper()

# ==================== FLIGHT SEARCH PARAMETERS ====================

SERP_PARAMS = {
    "api_key": SERP_API_KEY,
    "engine": "google_flights",
    "departure_id": departure_destination,
    "arrival_id": arrival_destination,
    "outbound_date": tomorrow,
    "return_date": six_month_from_today,
    "type": "1",  # Round trip
    "adults": "1",
    "currency": "USD",
}

# ==================== API REQUEST ====================

response = requests.get(SERP_API_ENDPOINT, params=SERP_PARAMS)
result = response.json()

# ==================== DEBUG RESPONSE ====================

print("\n=========== FULL RESPONSE ===========\n")
pprint(result)

# ==================== HANDLE NO FLIGHTS ====================

best_flights = result.get("best_flights", [])
other_flights = result.get("other_flights", [])

all_flights = best_flights + other_flights

if len(all_flights) == 0:
    print("\nNo flights found.")
    exit()

# ==================== FIND CHEAPEST FLIGHT ====================

cheapest_flight = None

for flight in all_flights:

    # Skip flights with missing price
    if "price" not in flight:
        continue

    if cheapest_flight is None:
        cheapest_flight = flight

    elif flight["price"] < cheapest_flight["price"]:
        cheapest_flight = flight

# ==================== HANDLE NO VALID PRICE ====================

if cheapest_flight is None:
    print("\nNo valid flight prices found.")
    exit()

# ==================== EXTRACT DATA ====================

lowest_price = cheapest_flight["price"]

origin_airport = cheapest_flight["flights"][0]["departure_airport"]["id"]

destination_airport = cheapest_flight["flights"][-1]["arrival_airport"]["id"]

departure_city = (
    cheapest_flight["flights"][0]["departure_airport"]["name"].split()[0]
)

departure_date = (
    cheapest_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
)

# Return date is not present in response
return_date = six_month_from_today

# ==================== PRINT CHEAPEST FLIGHT ====================

print("\n=========== CHEAPEST FLIGHT ===========\n")

print(f"Departure City: {departure_city}")
print(f"Origin Airport: {origin_airport}")
print(f"Destination Airport: {destination_airport}")
print(f"Departure Date: {departure_date}")
print(f"Return Date: {return_date}")
print(f"Lowest Price: ${lowest_price}")

# ==================== SHEETY API ====================

sheet_api_key = "YOUR_SHEETY_PROJECT_ID"

sheet_endpoint = f"https://api.sheety.co/{sheet_api_key}/flightDeals/sheet1"

bearer_auth_token = input("\nEnter Sheety Bearer Token: ")

bearer_headers = {
    "Authorization": f"Bearer {bearer_auth_token}"
}

# ==================== DATA TO SEND ====================

sheet_data = {
    "sheet1": {
        "city": departure_city,
        "iataCode": destination_airport,
        "lowestPrice": lowest_price
    }
}

# ==================== POST DATA ====================

response2 = requests.post(
    url=sheet_endpoint,
    json=sheet_data,
    headers=bearer_headers
)

# ==================== RESPONSE ====================

print("\n=========== SHEETY RESPONSE ===========\n")
print(response2.text)