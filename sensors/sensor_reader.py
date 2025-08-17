import soil_moisture
import temperature

from domain import TemperatureData, SensorData

def readSensors():

    temperature_data = temperature.getTemperature()
    soil_moisture_data = soil_moisture.readMoisturePercentageLevel()

    return SensorData(
        temperature=temperature_data.temperature_c,
        humidity=temperature_data.humidity,
        moisture=soil_moisture_data
    )
