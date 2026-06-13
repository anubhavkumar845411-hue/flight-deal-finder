# Flight Deal Finder ✈️

A Python application that monitors flight prices and sends SMS and Email alerts when cheaper flight deals are found.

## Features

- Search flights using APIs
- Compare current prices with stored prices
- Update lowest prices automatically
- Send SMS notifications using Twilio
- Send Email notifications
- Store flight data using Sheety
- Environment variable support with .env

## Technologies Used

- Python
- Requests
- Twilio API
- Sheety API
- Amadeus Flight API
- Python Dotenv

## Project Structure

```
flight_price_compare/
│
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
├── twillo.py
├── README.md
└── .gitignore
```

## How It Works

1. Fetch destination data from Google Sheets via Sheety.
2. Search for flight prices.
3. Compare current price with stored lowest price.
4. Update the lowest price if a cheaper flight is found.
5. Send SMS and Email alerts to users.

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file and add:

```env
AMADEUS_API_KEY=your_api_key
AMADEUS_API_SECRET=your_secret
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
```

## Author

Anubhav Kumar
Computer Science Student | Python Developer