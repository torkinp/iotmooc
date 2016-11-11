# Blink an LED while a button is not pressed, 
# have the LED solid on while the button IS pressed.

import RPi.GPIO as GPIO # import GPIO Library 
import time ## Import 'time' library. Allows us to use 'sleep' 

GPIO.setmode(GPIO.BCM) # set board mode to Broadcom 
GPIO.setup(17, GPIO.OUT) # set up pin 17, for the LED
# set pin 16 as input, for the push button
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set 16 for input

try:
    while True:
        # button pressed?
        if not((GPIO.input(16))):
            GPIO.output(17, True)
            
        # button not pressed
        else:
            GPIO.output(17, not(GPIO.input(17))) 
            time.sleep(0.2) 

finally: 
    GPIO.cleanup()
