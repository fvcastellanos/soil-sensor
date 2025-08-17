from bottle import post, get, route, request, HTTPResponse
import uuid
import logging

from sensors import temperature

@get("/temperature")
def get_temperature():

    data = temperature.getTemperature()

    body = {
        "temperature": data.temperature_c,
        "humidity": data.humidity
    }

    return HTTPResponse(status = 200, body = body)

