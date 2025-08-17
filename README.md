# Sensor Reader

Simple web API that reads temperature, humidity, soil moisture using the following components:

* DHT11
* MCP3008 ADC
* Soil Moisture Reader

## Hardware Board:

Raspberry Pi 3B

## Application Setup

Install `virtualenv`

```
pip install virtualenv
```

Define a virtual environment

```
virtualenv venv
```

Install environment specific dependencies defined in `requirements.txt`:

```
pip install -r requirements.txt
```

