#!/usr/bin/python3.9 

import RPi.GPIO as GPIO
import time


GPIO_PORT24 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PORT24, GPIO.OUT)

for i in  range(0,3):
    GPIO.output(GPIO_PORT24, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(GPIO_PORT24, GPIO.LOW)
    time.sleep(0.1)
GPIO.cleanup()
