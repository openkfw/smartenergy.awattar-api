"""
Electricity Maps API module, documentation:
https://static.electricitymaps.com/api/docs/index.html
"""


import requests

from .validations import validate_empty_string


# pylint: disable=too-few-public-methods
class ElectricityMapApi:
    """
    Class providing methods for getting CO2 forecast for a zone.
    """

    def __init__(self, host: str, token: str, timeout: int = 5) -> None:
        validate_empty_string(host, "host")
        validate_empty_string(token, "token")
        self.host: str = host
        self.token: str = token
        self.timeout: int = timeout

    def __query_forecast_api(self, path: str, zone: str) -> dict:
        try:
            url = f"{self.host}/{path}?zone={zone}"
            headers = {"X-BLOBR-KEY": f"{self.token}"}

            status_request = requests.get(
                    url,
                    headers=headers,
                    timeout=self.timeout)

            status = status_request.json()
            return status
        except (
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ConnectionError,
        ):
            return {"success": False,
                    "msg": "Request couldn't connect or timed out"}

    def get_co2_forecast(self, zone: str) -> dict:
        """Get the CO2 forecast for a zone"""
        response = self.__query_forecast_api("carbon-intensity/forecast", zone)

        if response is None or response.get("success") is False:
            raise RuntimeError(f"Request failed with: {response}")

        return response
