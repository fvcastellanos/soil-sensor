# Sensor Reader

Simple web API that reads temperature, humidity, soil moisture using the following components:

* DHT11
* MCP3008 ADC
* Soil Moisture Reader

## Hardware Board:

Raspberry Pi 3B

### DHT11 Setup

If using DHT11 temperature sensor and a Raspberry Pi v3 it is necessary to configure DHT11 Overlay

```
sudo nano /boot/firmware/config.txt
```

Append the following line at the end of the file:

```
dtoverlay=dht11,gpiopin=<PIN>
```

Where `PIN` is the GPIO pin where the sensor data pin is connected to the RPi. Once updated the file, reboot the board.

```
sudo reboot now
```

#### Test changes

Values captured from the DHT11 sensor can be accessed by displaying the content of the following files:

```
cat /sys/bus/iio/devices/iio:device0/in_temp_input
```

And for humidity

```
cat /sys/bus/iio/devices/iio:device0/in_humidityrelative_input
```

Values captured are multiplied by `1000` so that means that 2100 refers to 21.0C as well for humidity values


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

