import sys
import temperature
import logging4

from retry import retry

logger = logging4.Logger(name = "AppLogger")
formatter = '[[time]] - [[name]] - [[level_name]] - [[msg]]'

logger.add_channel(filename=sys.stdout, level=logging4.INFO, formatter=formatter)

def main():

    logger.info(f"Reading temperature sensor DHT11")
    data = temperature.getTemperature()
    logger.info(f"Temp C: {data.temperature_c} - Humidity: {data.humidity}")


if __name__ == "__main__":
    main()


