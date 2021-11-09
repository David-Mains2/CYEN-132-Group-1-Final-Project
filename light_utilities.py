#importing functions for code
import RPi.GPIO as GPIO
from time import sleep

###this section is for setup and basic starting function
#sets up lights for appropriate output types
def set_up(lights):
    GPIO.setmode(GPIO.BCM) #setting pins to appropriate IO types
    GPIO.setwarnings(False)
    for i in lights:
        GPIO.setup(i, GPIO.OUT)

def clean():
    GPIO.cleanup()


#function to turn all lights on
def on_all(lights):
    for i in lights:
        GPIO.output(i, GPIO.HIGH)

        
#function to turn all lights off
def off_all(lights):
    for i in lights:
        GPIO.output(i, GPIO.LOW)


#FUNCTIONS FOR  DIFFERENT ALARM STATUSS
#function for normal status
def normal(green_leds):
    #ensure lights and pins are set up corectly
    set_up(green_leds)
    on_all(green_leds)

#function for warning signal
def warning(red_leds):
    set_up(red_leds)
    while (True):
        on_all(red_leds)
        sleep(0.5)
        off_all(red_leds)
        sleep(0.5)

