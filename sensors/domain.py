from dataclasses import dataclass

@dataclass
class TemperatureData:
    temperature_c: float
    temperature_f: float
    humidity: float

@dataclass
class SensorData:
    temperature: float
    humidity: float
    moisture: float
