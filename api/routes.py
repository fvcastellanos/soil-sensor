# from bottle import post, get, route, request, HTTPResponse, response, HTTPError

from sensors import temperature, soil_moisture

# @get("/temperature")
def get_temperature():

    try:

        data = temperature.getTemperature()

        return {
            "temperature": data.temperature_c,
            "humidity": data.humidity
        }

        # body = {
        #     "temperature": data.temperature_c,
        #     "humidity": data.humidity
        # }

        # return buildResponse(body)

    except: 

        return ""

        # return buildServerErrorResponse("noooo!!!")

# @get("/moisture")
def get_moisture():

    try:
        data = soil_moisture.readMoisturePercentageLevel()

        body = {
            "moisture": data
        }

        return buildResponse(body)

    except:

        return buildServerErrorResponse("Unable to retrieve soil moisture data")

# @get("/ping")
def ping():

    response.set_header('Content-Type', 'application/json')
    return {
        "pong": True
    }


def buildServerErrorResponse(message: str) -> HTTPError:
    
    body = {
        "message": message
    }

    return HTTPError(body = body, status = 500, headers = {
        'Content-Type', 'application/json'
    })

def buildResponse(body: dict) -> HTTPResponse:

        headers = {
            "Content-Type": "application/json"
        }

        return HTTPResponse(status=200, body=body, headers=headers)