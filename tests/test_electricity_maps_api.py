"""Test cases for the electricity maps api module"""
from unittest import mock
import pytest

from electricity_maps_api.electricity_maps_api import ElectricityMapApi

ELECTRICITY_MAPS_RESPONSE_DE = {
    "zone": "DE",
    "forecast": [
        {"carbonIntensity": 600, "datetime": "2022-12-14T15:00:00.000Z"},
        {"carbonIntensity": 610, "datetime": "2022-12-14T16:00:00.000Z"},
        {"carbonIntensity": 625, "datetime": "2022-12-14T17:00:00.000Z"},
        {"carbonIntensity": 640, "datetime": "2022-12-14T18:00:00.000Z"},
    ],
    "updatedAt": "2022-12-14T14:51:00.960Z",
}


ELECTRICITY_MAPS_API_URL = "http://localhost:3000"
TOKEN = "TOKEN"
ZONE = "DE"


# pylint: disable=unused-argument
def mocked_requests_get(*args, **kwargs):
    """Module handling mocked API requests"""

    # pylint: disable=too-few-public-methods
    class MockResponse:
        """Class handling mocked API responses"""

        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            """Return data as a JSON"""
            return self.json_data

    if args[0] == f"{ELECTRICITY_MAPS_API_URL}/carbon-intensity/forecast?zone={ZONE}":
        return MockResponse(ELECTRICITY_MAPS_RESPONSE_DE, 200)

    return MockResponse(None, 404)


@mock.patch(
    "requests.get",
    mock.Mock(side_effect=mocked_requests_get),
)
def test_get_co2_forecast() -> None:
    """Test if the forecast data is returned"""
    api = ElectricityMapApi(ELECTRICITY_MAPS_API_URL, TOKEN)
    assert api.get_co2_forecast("DE") == ELECTRICITY_MAPS_RESPONSE_DE


@mock.patch(
    "requests.get",
    mock.Mock(side_effect=mocked_requests_get),
)
def test_request_status_error() -> None:
    """Test if API call fails"""
    api = ElectricityMapApi("http://localhost:3001", TOKEN)
    with pytest.raises(Exception) as exception:
        api.get_co2_forecast("DE")
    assert str(exception.value) == "Request failed with: None"
