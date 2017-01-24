#!/usr/bin/python
import os
import RPi.GPIO as GPIO ## Import GPIO Library
from time import sleep ## Import 'time' library.  Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering

GPIO.setup(10, GPIO.IN) ## Setup GPIO pin 16 to IN (button 1)

GPIO.setup(17, GPIO.OUT) ## Setup GPIO pin 11 to OUT (LED 1)
GPIO.setup(27, GPIO.OUT) ## Setup GPIO pin 13 to OUT (LED 2)
GPIO.output(17, GPIO.LOW) ## LED 1 Off
GPIO.output(27, GPIO.LOW) ## LED 2 Off

print("--------------")
print(" Button + GPIO ")
print("--------------")

print GPIO.input(10)
while True:
    if ( GPIO.input(10) == False):
        print ("Button Pressed")
        os.system('date')
        GPIO.output(17, GPIO.HIGH) #Blink 
        GPIO.output(27, GPIO.LOW)
        sleep(1)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH)
        sleep(1)
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        sleep(1)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH)
        print GPIO.input(10)
        sleep(5)
    else:
        os.system('clear')
        print ("Watiing for you to press a button")
sleep(1)
