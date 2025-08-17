from fastapi import FastAPI, HTTPException

from sensors import temperature, soil_moisture

app = FastAPI()

@app.get("/temperature")
def get_temperature():

    try:
        data = temperature.get_temperature()

        return {
            "temperature": data.temperature_c,
            "humidity": data.humidity
        }

    except: 

        raise HTTPException(status_code = 500, detail = "Unable to retrieve temperature / humidity data")

@app.get("/moisture")
def get_moisture():

    try:

        data = soil_moisture.readMoisturePercentageLevel()

        return {
            "moisture_percentage": data
        }
    except:
        raise HTTPException(status_code = 500, detail = "Unable to retrieve soild moisture data")

@app.get("/ping")
def ping():

    return {
        "pong": True
    }
