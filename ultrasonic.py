import RPi.GPIO
import time


def measureDistance(trigPin, echoPin):
    GPIO.output(trigPin, 0)
    time.sleep(2E-6)
    GPIO.output(trigPin, 1)
    time.sleep(10E-6)
    GPIO.output(trigPin, 0)
    while GPIO.input(echoPin)==0:
        pass
    start = time.time()
    while GPIO.input(echoPin)==1:
        pass
    end = time.time()
    travelTime = (end-start)*1E6
    travelDistance = (34300 * travelTime) / 1E6
    return travelDistance / 2


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
    