"""Green Energy API examples"""

import os

from dotenv import load_dotenv
from green_energy_api.green_energy_api import GreenEnergyApi

load_dotenv()

green_energy = GreenEnergyApi(
    os.getenv("ENERGY_DATA_API_URL"),
)
print(green_energy.get_electricity_price())
