import RPi.GPIO
import time

in_pin = 11

GPIO.setmode(GPIO.BOARD)
GPOI.setup(in_pin, GPIO.IN)

while True:
    sensor = GPIO.in_pin(input)

    if sensor == 1:
        print(sensor)
        sleep(0.1)

    elif sensor == 0:
        print("it's zero now: "+sensor)

    else:
        print(sensor)

