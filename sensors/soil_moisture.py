import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import logging

logger = logging.getLogger("moisture.module")

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
#mcp = Adafruit_MCP3008.MCP3008(clk = 11, cs = 8, miso = 9, mosi = 10)

# ADC input channel for Analog output
CHANNEL = 0

MAX_VALUE = 1023

def readMoistureRawLevel():
    return mcp.read_adc(CHANNEL)

def readMoisturePercentageLevel():

    logger.info("Reading soil moisture value")
    raw_value = readMoistureRawLevel()
    logger.info(f"Raw value: {raw_value}")

    # percentage = ((MAX_VALUE - raw_value) / MAX_VALUE) * 100
    percentage = ((MAX_VALUE - raw_value) * 100) / MAX_VALUE

    return round(percentage, 2)
