import board
import adafruit_dht

from domain import TemperatureData
from retry import retry

adafruit_dht.DHT11.use_pulseio = False
sensor = adafruit_dht.DHT11(board.D17)

@retry(Exception, tries=3, delay=2)
def getTemperature() -> TemperatureData:

    try:
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity
        return TemperatureData(temperature_c, temperature_f, humidity)

    except Exception as error:
        raise error

    finally:
        sensor.exit()

