"""Electricity Maps API examples"""

import os

from dotenv import load_dotenv
from electricity_maps_api.electricity_maps_api import ElectricityMapApi

load_dotenv()

electricity_map = ElectricityMapApi(
        os.getenv("ELECTRICITY_MAPS_API_URL"),
        os.getenv("ELECTRICITY_MAPS_API_TOKEN"))
print(electricity_map.get_co2_forecast("DE"))
