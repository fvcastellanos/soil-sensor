import sys
import logging4

from bottle import run

from sensors import temperature
from sensors import soil_moisture

import routes

logger = logging4.Logger(name = "AppLogger")
formatter = '[[time]] - [[name]] - [[level_name]] - [[msg]]'

logger.add_channel(filename=sys.stdout, level=logging4.INFO, formatter=formatter)

# def main():

#     logger.info(f"Reading temperature sensor DHT11")
#     data = temperature.getTemperature()
#     logger.info(f"Temp C: {data.temperature_c} - Humidity: {data.humidity}")

#     logger.info("Reading analog value")
#     moisture = soil_moisture.readMoisturePercentageLevel()
#     rawValue = soil_moisture.readMoistureRawLevel()
#     logger.info(f"Soil Moisture: {moisture}% - Raw value: {rawValue}")


def main():

    run(host='0.0.0.0', port=9080)

if __name__ == "__main__":
    main()
