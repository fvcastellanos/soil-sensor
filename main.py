
import sys
import logging4

# from bottle import run

from sensors import temperature, soil_moisture
from api import routes

logger = logging4.Logger(name = "AppLogger")
formatter = '[[time]] - [[name]] - [[level_name]] - [[msg]]'

logger.add_channel(filename=sys.stdout, level=logging4.INFO, formatter=formatter)

# def main():

#     run(host='0.0.0.0', port=9080)

# if __name__ == "__main__":
#     main()
