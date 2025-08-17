from bottle import post, get, route, request, HTTPResponse, response
import uuid
import logging

from sensors import temperature
from sensors import soil_moisture

@get("/temperature")
def get_temperature():

    try:

        data = temperature.getTemperature()

        body = {
            "temperature": data.temperature_c,
            "humidity": data.humidity
        }

        response.set_header('Content-Type', 'application/json')
        return body

    except: 

        abort(500, 'Nooooo!!!')
    # return HTTPResponse(status = 200, body = body)

@get("/moisture")
def get_moisture():

    data = soil_moisture.readMoisturePercentageLevel()

    body = {
        "moisture": data
    }

    # return HTTPResponse(status = 200, body = body)
    response.set_header('Content-Type', 'application/json')
    return body


@get("/ping")
def ping():

    response.set_header('Content-Type', 'application/json')
    return {
        "pong": True
    }