import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BOARD)
    trigPin = 23
    echoPin = 24
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)