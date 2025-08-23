from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sensors import temperature, soil_moisture, relay

import logging

logging.basicConfig(
    level=logging.INFO,  # Set the log level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Configure relay
relay.setupPinOut()

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods = ["*"],
    allow_headers = ["*"] 
)

class RelayAction(BaseModel):
    action: str

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
    except Exception as error:

        logger.error(error)
        raise HTTPException(status_code = 500, detail = "Unable to retrieve soild moisture data")

@app.get("/ping")
def ping():

    return {
        "pong": True
    }

@app.post("/water-pump")
def water_pump(action: RelayAction):

    try:
        if (action.action.lower() == "activate"):

            relay.activate()
        else:

            relay.deactivate()

        return {
            "action": "done"
        }

    except Exception as error:

        logger.error(error)
        raise HTTPException(status_code = 500, detail = "Unable to activate/deactivate water pump")

