import RPi.GPIO as GPIO # GPIO lib
import time # Used to provide sleep function

GPIO.setmode(GPIO.BCM) # Use the BCM naming convention

# set up pin 17 for the LED
GPIO.setup(17, GPIO.OUT)
p = GPIO.PWM(17, 100)# set up PWM, channel=17 (led pin) frequency=100Hz 
p.start(0)

ledlevel = 0 # used to set the pwm duty cycle from 0% to 100%
inc = -2  # the value to adjust the duty cycle by

# the assignment requires the time from max brightness to min
# brightness be "al least one second", so take variable "inc"
# and use it to calculate the sleep time delay
sleeptime = 2 * (1 / abs(100 / inc))

try:
    while True:
        # If the led has reached minimum or maximum brightness,
        # change increment to be +ve or -ve so the brightness will
        # start changing in teh other direction.
        if (ledlevel == 0 or ledlevel == 100):
            inc = inc * -1

        ledlevel += inc # change Duty Cycle
        p.ChangeDutyCycle(ledlevel) 
        time.sleep(sleeptime)
        
except KeyboardInterrupt:
    pass
        
p.stop() # stop pwm 
GPIO.cleanup() # tidy GPIO

