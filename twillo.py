import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


class Message:

    def send_message(self, flight_details_message):

        account_sid = os.getenv("Account_SID")
        auth_token = os.getenv("Auth_Token")
        twilio_phone_no = os.getenv("twillio_whatsapp_no")

        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(
                body=flight_details_message,
                from_=f'whatsapp:{twilio_phone_no}',
                to='whatsapp:+917970797683'
            )

            print("Message SID:", message.sid)
            print("Message Status:", message.status)

        except Exception as e:
            print("Error:", e)