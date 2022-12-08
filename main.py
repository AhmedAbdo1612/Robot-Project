import RPi.GPIO as GPIO
import time
from ultrasonic import *

def main():
    GPIO.setmode(GPIO.BCM)
    trigPin = 23
    echoPin = 24
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

    try:
        while True:
            print(measureDistance(trigPin, echoPin))
            time.sleep(.2)
    except KeyboardInterrupt():
        GPIO.cleanup()
        print("ALL CLEAR!")