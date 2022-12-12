import RPi.GPIO as GPIO
import time

in_pin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in_pin, GPIO.IN)

while True:
    sensor = GPIO.input(inp_pin)

    if sensor == 1:
        print(sensor)
        sleep(0.1)

    elif sensor == 0:
        print("it's zero now: "+sensor)

    else:
        print(sensor)

