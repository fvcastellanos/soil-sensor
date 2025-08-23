import RPi.GPIO as io # using RPi.GPIO

PIN27 = 27

def setupPinOut():
    io.setmode(io.BCM)
    io.setup(PIN27, io.OUT) # make pin into an output

def activate():
    io.output(PIN27, 1)

def deactivate():
    io.output(PIN27, 0)
