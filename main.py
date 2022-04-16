#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch

# import requests

#
#
# HEADER = {
#     "Authorization": "Bearer nxxcbhdhfhsbnckjsckjndsklcbjdsmckbsdhblbdfhksmf"
# }
#
#
# URL = "https://api.sheety.co/e7b04df5e28a766787e1edcd49ebe0a1/flightDealsTracker/prices"
#
#
# response = requests.get(url=URL, headers=HEADER)
# response.raise_for_status()
# data = response.json()
# print(data["prices"])

dm = DataManager()

city_name = dm.sheets_data
pprint(city_name)






