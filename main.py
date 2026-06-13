import requests_cache
requests_cache.install_cache(
    'flight_cache',
    expire_after=3600
)

from data_manager import Datamanager
from flight_search import Flightsearch
from twillo import Message
from dotenv import load_dotenv
from notification_manager import NotificationManager

load_dotenv()

flight_search_data = Flightsearch()
data_manager = Datamanager()
sheet_data = data_manager.get_data()
send_message = Message()
Email_notification = NotificationManager()

# ======this to get the customer emails =========================
customer = data_manager.get_customer_email()
customer_email = []
for user in customer:
    email = user.get('whatIsYourEmail?')
    if email and "@" in email:
        customer_email.append(email)
print(customer_email)
# =====================================================================
ORIGIN_DEPATURE_AIRPORT = "CDG"
for i in range(len(sheet_data)):

    DESTINATION_CODE = sheet_data[i]["iataCode"]

    if DESTINATION_CODE == ORIGIN_DEPATURE_AIRPORT:
        continue

    # here we check for the flight
    endpoint, prams = flight_search_data.check_flight(ORIGIN_DEPATURE_AIRPORT, DESTINATION_CODE)
    flight_details = flight_search_data.get_cheapest_flight(endpoint , prams)
    print(f"flight details = {flight_details}")

    # ========================= Compare Price =========================

    ticket_price = flight_details[7]

    if ticket_price == "N/A":
        continue

    lowest_price = int(sheet_data[i].get("lowestPrice", 999999))
    print(f"Ticket Price = {ticket_price}")
    print(f"Lowest Price = {lowest_price}")
    if ticket_price <= lowest_price:
        print(f"Lower price flight found to {sheet_data[i]['city']}!")

        data_manager.update_lowest_price(
            row_id=sheet_data[i]["id"],
            new_price=ticket_price
        )

        flight_message = (
            f"Flight Alert!\n\n"
            f"Only ${ticket_price} to fly\n"
            f"From: {flight_details[1]}\n"
            f"To: {flight_details[3]}\n"
            f"Departure Date: {flight_details[4]}\n"
            f"Return Date: {flight_details[5]}"
        )

        send_message.send_message(flight_message)

        # ✅ EMAIL ONLY HERE
        for email in customer_email:
            try:
                Email_notification.send_email(email, flight_message)
            except Exception as e:
                print(f"Email failed for {email}: {e}")

    else:
        print("No better deal found")