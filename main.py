from sensors import temperature, soil_moisture
import logging

logging.basicConfig(
    level=logging.INFO,  # Set the log level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def main():

    logger.info("Reading sensors")

    t_data = temperature.get_temperature()
    t_moisture = soil_moisture.readMoisturePercentageLevel()

    logger.info(f"Temp: {t_data.temperature_c}C / {t_data.temperature_f}F, Humidity: {t_data.humidity}%")
    logger.info(f"Soil Moisture: {t_moisture}%")


if __name__ == "__main__":
    main()
