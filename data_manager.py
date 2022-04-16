import requests
from pprint import pprint

# HEADER = {
#     "Authorization": "Bearer nxxcbhdhfhsbnckjsckjndsklcbjdsmckbsdhblbdfhksmf"
# }
#
# URL = "https://api.sheety.co/e7b04df5e28a766787e1edcd49ebe0a1/flightDealsTracker/prices"


class DataManager:
    def __init__(self):

        self.HEADER = {
            "Authorization": "Bearer nxxcbhdhfhsbnckjsckjndsklcbjdsmckbsdhblbdfhksmf"
        }

        self.URL = "https://api.sheety.co/e7b04df5e28a766787e1edcd49ebe0a1/flightDealsTracker/prices"

        response = requests.get(url=self.URL, headers=self.HEADER)
        response.raise_for_status()
        data = response.json()
        self.sheets_data = data["prices"]



    # def update_data(self):
    #     url_update = "https://api.sheety.co/e7b04df5e28a766787e1edcd49ebe0a1/flightDealsTracker/prices/[Object ID]"
    #
    #     response = requests.put(url=url_update, params= )
