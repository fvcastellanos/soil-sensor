import logging

import board

from .domain import TemperatureData

logger = logging.getLogger("uvicorn.error")

TEMPERATURE_BUS = "/sys/bus/iio/devices/iio:device0/in_temp_input"
HUMIDITY_BUS = "/sys/bus/iio/devices/iio:device0/in_humidityrelative_input"

def get_temperature() -> TemperatureData:

    try:

        temperature_c = read_bus(TEMPERATURE_BUS)/1000
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = read_bus(HUMIDITY_BUS)/1000

        return TemperatureData(temperature_c, temperature_f, humidity)

    except Exception as error:
        logger.error(f"Error reading temperature: {error}")
        raise error

def read_bus(file_name: str):

    file = open(file_name, "rt")
    value = int(file.readline())
    file.close()

    return value
