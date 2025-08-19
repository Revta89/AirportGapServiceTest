from typing import List

from api.controllers.base_controller import BaseController
from requests import Response


class AirportGapClient(BaseController):
    def __init__(self):
        super().__init__(
            base_url='https://airportgap.com/api',
            headers={'Accept': 'application/json',
                     'Content-Type': 'application/json'})

    def get_airports(self) -> Response:
        """
        Get all airports
        return: Response containing all airports data
        """
        return self.get('/airports')

    def get_airport_names(self) -> List:
        """
        Get all airport names
        return: List containing airport names
        """
        response = self.get_airports()
        self.assert_response_code(response, 200)
        return [airport["attributes"]["name"] for airport in response.json().get("data", [])]

    def get_distance(self, from_airport: str, to_airport: str) -> Response:
        """
        Calculate distance between two airports
        @param from_airport: code of departure airport
        @param to_airport: code of arrival airport
        return: Response containing distance data
        """
        payload = {
            "from": from_airport,
            "to": to_airport
        }
        response = self.post("/airports/distance", payload)
        self.assert_response_code(response, 200)
        return response
