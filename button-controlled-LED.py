import RPi.GPIO as GPIO ## Import GPIO Library
from time import sleep ## Import 'time' library.  Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering

GPIO.setup(16, GPIO.IN) ## Setup GPIO pin 16 to IN (button 1)
GPIO.setup(18, GPIO.IN) ## Setup GPIO pin 18 to IN (button 2)

GPIO.setup(11, GPIO.OUT) ## Setup GPIO pin 11 to OUT (LED 1)
GPIO.setup(13, GPIO.OUT) ## Setup GPIO pin 13 to OUT (LED 2)
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)

# State – decides what LED should be on and off
state = 0

# Increment – the direction of states
inc = 1

while True:

# State toggle button is pressed
if ( GPIO.input(16) == True ):

if (inc == 1):
state = state + 1;
else:
state = state – 1;

# Reached the max state, time to go back (decrement)
if (state == 2):
inc = 0
# Reached the min state, go back up (increment)
elif (state == 0):
inc = 1

if (state == 1):
GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)
elif (state == 2):
GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
else:
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
print(“pressed B1 “, state)

# Reset button is pressed
if ( GPIO.input(18) == True ):

state = 0
inc = 1
GPIO.output(11, GPIO.LOW)
GPIO.output(13, GPIO.LOW)

print(“pressed B2 “, state)

sleep(0.2);
