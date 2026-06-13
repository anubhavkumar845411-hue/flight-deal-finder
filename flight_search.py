import os
import requests
from dotenv import load_dotenv
from datetime import datetime,timedelta
load_dotenv()
from pprint import pprint
# ==========================datetime =======================
class Flightsearch:
    def __init__(self):
        self.tomorrow = (datetime.now()+timedelta(days=1)).strftime("%Y-%m-%d")
        self.six_month_from_today = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

# =====================Serp Api ========================
    def check_flight(self,Departure,Arrival):
        SERP_ENDPOINT = os.getenv("serp_endpoint")
        SERP_API = os.getenv("serp_api")
        Departure_id = Departure
        Arrival_id = Arrival
        SERP_PRAMS = {
            "api_key":SERP_API,
            "engine":"google_flights",
            "departure_id": Departure_id.upper(),
            "arrival_id" : Arrival_id.upper(),
            "currency" :"USD",
            "type" : 1,
            "outbound_date": self.tomorrow,
            "return_date" : self.six_month_from_today
        }
        return SERP_ENDPOINT, SERP_PRAMS

# =============================flightsearch =================================

    def get_cheapest_flight(self, endpoint, params):
        responce = requests.get(endpoint,params=params)
        result = responce.json()
        all_flights = result.get("best_flights", []) + result.get("other_flights", [])
        # check if flights exist
        if "best_flights" not in result:
            print("No flights found")
            return ("N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A")

        chepest_flight_PRICE = 516561556
        chepest_flight = {}
        for flights in all_flights:
            # if flights["price"] < chepest_flight_PRICE:
                try:
                    if flights["price"] < chepest_flight_PRICE:
                        chepest_flight_PRICE = flights["price"]
                        chepest_flight = flights
                except KeyError:
                    continue


        departure_name = chepest_flight["flights"][0]["departure_airport"]["name"]
        departure_id = chepest_flight["flights"][0]["departure_airport"]["id"]
        arrival_name = chepest_flight["flights"][-1]["arrival_airport"]["name"]
        arrival_id = chepest_flight["flights"][-1]["arrival_airport"]["id"]
        out_date = chepest_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
        return_date = self.six_month_from_today
        if "layovers" in chepest_flight:
            layovers_name = chepest_flight["layovers"][0]["name"]
        else:
            layovers_name = "Direct Flight"
        Ticket_price  = chepest_flight["price"]
        airline_name = chepest_flight["flights"][0]["airline"]
        total_duration = chepest_flight["total_duration"]
        return (
            departure_name,
            departure_id,
            arrival_name,
            arrival_id,
            out_date,
            return_date,
            layovers_name,
            Ticket_price,
            airline_name,
            total_duration
        )

# ==================how to exucute it =======================================
f1 = Flightsearch()
endpoint , prams =f1.check_flight("cdg","aus")
f1.get_cheapest_flight(endpoint,prams)