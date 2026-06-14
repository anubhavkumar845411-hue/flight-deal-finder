# ✈️ Flight Deal Finder

A Python automation project that monitors flight prices and automatically sends SMS and Email alerts when cheaper flight deals are found.

## 🎥 Project Demo

[![Flight Deal Finder Demo]](https://youtu.be/QHnp20bQTVE)

👉

---

## Features

* Search flight prices using the Amadeus Flight API
* Compare current flight prices with stored prices
* Automatically update the lowest recorded price
* Send SMS notifications using Twilio
* Send Email notifications to subscribed users
* Store flight and customer data using Sheety
* Cache API requests to reduce unnecessary API calls
* Secure credential management using `.env`

---

## Technologies Used

* Python
* Requests
* Requests Cache
* Amadeus Flight API
* Twilio API
* Sheety API
* SMTP
* Python Dotenv

---

## Project Structure

```text
flight_price_compare/
│
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
├── twilio.py
├── requirements.txt
├── thumbnail.png
├── README.md
├── .gitignore
└── .env
```

---

## How It Works

1. Fetch destination data from Google Sheets using Sheety.
2. Retrieve customer email addresses.
3. Search for available flights using the Amadeus API.
4. Compare the current flight price with the stored lowest price.
5. Update Google Sheets when a lower price is found.
6. Send SMS alerts using Twilio.
7. Send Email notifications to all subscribed users.

---


## Environment Variables

Create a `.env` file and add:

```env
AMADEUS_API_KEY=your_api_key
AMADEUS_API_SECRET=your_secret

TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token

EMAIL_ADDRESS=your_email
EMAIL_PASSWORD=your_password

SHEETY_ENDPOINT=your_sheety_endpoint
```

---

## Run the Project

```bash
python main.py
```

---

## Example Notification

```text
Flight Alert!

Only $150 to fly

From: Paris (CDG)
To: London (LHR)

Departure Date: 15 Jul 2026
Return Date: 25 Jul 2026
```

---

## Future Improvements

* Web Dashboard
* User Authentication
* Multiple Departure Airports
* WhatsApp Notifications
* Telegram Notifications
* Price Trend Analysis

---

## Author

**Anubhav Kumar**

Computer Science Student | Python Developer

Focused on Python Automation, APIs, Backend Development, and AI Projects.

---

⭐ If you found this project useful, consider giving it a star.
