import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:

    def send_email(self, email, message):

        my_email = os.getenv("MY_EMAIL")
        my_password = os.getenv("MY_PASS")

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()

        connection.login(user=my_email, password=my_password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:New Flight Deal!\n\n{message}"
        )

        connection.quit()