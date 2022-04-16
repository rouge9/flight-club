import requests

URL = "https://api.sheety.co/e7b04df5e28a766787e1edcd49ebe0a1/flightDealsTracker/prices"
HEADER = {
    "Authorization": "Bearer nxxcbhdhfhsbnckjsckjndsklcbjdsmckbsdhblbdfhksmf"
}


class FlightData:
    def __init__(self):
        self.parameters = {
            "price": {
                "city": "Rome",
                "iata code": "500",
                "lowest price": "",
            }
        }

        self.add_data()









    def add_data(self):

        response = requests.post(url=URL, json=self.parameters, headers=HEADER)
        print(response.text)

