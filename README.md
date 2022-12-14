# smart_energy.electricity_maps_api

A python library to access the Electricity Maps API. Refer also to the [Electricity Maps API Docs](https://static.electricitymaps.com/api/docs/index.html). This repo provides functionality for:

- Getting CO2 intensity forecast information for a specific geographical zone (see all available zones [here](https://api.electricitymap.org/v3/zones))

## Installing the library locally

Python 3 is recommended for this project.

```bash
python -m pip install -e .
```

> **This is needed for the first time when working with the library/examples/tests.**

## Example usage

```bash
ELECTRICITY_MAPS_API_URL="https://api-access.electricitymaps.com/REPLACE_ME" ELECTRICITY_MAPS_API_TOKEN="REPLACE_ME" python3 examples/simple.py
```

or

```python
from electricity_maps_api.electricity_maps_api import ElectricityMapApi

electricity_map = ElectricityMapApi('provide_api_url', 'provide_api_token')
# or you can define additional optional parameters
# electricity_map = ElectricityMapApi('provide_api_url', 'provide_api_token', timeout=10)

print(electricity_map.get_co2_forecast("DE"))
```

## Development

### Installing required pip packages

```bash
python pip install -r requirenments.txt
pre-commit install -t pre-push
```

### Linting

```bash
pylint electricity_maps_api/*.py tests/*.py examples/*.py
```

### Unit testing

```bash
pytest tests/*.py

# show logs
pytest -o log_cli=true

# code coverage
pytest --durations=10 --cov-report term-missing --cov=electricity_maps_api tests
```
