import requests
import os
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()
SHEETY_PRICES_ENDPOINT ="https://api.sheety.co/13965864f2abcc749d22d3d991258f5b/cheapFlightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.USER_NAME = os.getenv('USER_NAME')
        self.PASSWORD = os.getenv('PASSWORD')
        self._auth = (self.USER_NAME, self.PASSWORD)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT,
            auth=self._auth
        )
        self.destination_data = response.json()['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response=requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                auth=self._auth,
                json=new_data
                )
            print(response.text)