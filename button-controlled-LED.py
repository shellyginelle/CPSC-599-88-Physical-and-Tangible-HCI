#!/usr/bin/python
import os
import RPi.GPIO as GPIO ## Import GPIO Library
from time import sleep ## Import 'time' library.  Allows us to use 'sleep'

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) ## Use BOARD pin numbering

GPIO.setup(10, GPIO.IN) ## Setup GPIO pin 10 to IN (button 1)
GPIO.setup(18, GPIO.OUT) ## Setup GPIO pin 18 to OUT (LED 1)

print GPIO.input(10)
while True:
    if (GPIO.input(10)):    
        print ("Button Pressed")
        GPIO.output(18, GPIO.LOW)
        sleep(1)
        GPIO.output(18, GPIO.HIGH)
        sleep(1)
        GPIO.output(18, GPIO.LOW)
        print GPIO.input(10)
        sleep(5)
    else:
        os.system('clear')
        print ("Watiing for you to press a button")
sleep(1)
