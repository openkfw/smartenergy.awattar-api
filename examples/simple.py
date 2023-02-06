"""Awattar API API examples"""

import os

from dotenv import load_dotenv
from awattar_api.awattar_api import AwattarApi

load_dotenv()

awattar = AwattarApi(
    os.getenv("ENERGY_DATA_API_URL"),
)
print(awattar.get_electricity_price())
