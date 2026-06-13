import requests
from dotenv import load_dotenv
import os


load_dotenv()

sheet_endpoint = os.getenv("Sheet_Endpoint")
Username = os.getenv("Sheet_username")
Password = os.getenv("Sheet_password")
sheet_user_endpoint = os.getenv("sheet_user_endpoint")

class Datamanager :
    def get_customer_email(self):
        responce = requests.get(url=sheet_user_endpoint,auth=(Username,Password))
        result = responce.json()
        return result["users"]

    def get_data(self):
        responce = requests.get(url=sheet_endpoint,auth=(Username,Password))
        result = responce.json()
        return result["sheet1"]

    def update_lowest_price(self,row_id,new_price):
        prams = {
            "sheet1" : {
            "lowestPrice": new_price
            }
        }
        responce1 = requests.put(url=f"{sheet_endpoint}/{row_id}",json=prams,auth=(Username,Password))
        print(responce1.text)
       


