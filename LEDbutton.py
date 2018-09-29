# Tutorial from youtube link below:
# https://www.youtube.com/watch?v=ntKI2Nj-hSU&list=PLNnwglGGYoTvy37TSGFlv-aFkpg7owWrE&index=22

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount = 3
count = 0
LEDPin = 22     # GPIO22 is where the LED's longer +ve pin is connected to.
buttonPin = 5   # GPIO5 is where one of the button pin is connected to.

# Setup what the GPIO22 is.
GPIO.setup(LEDPin, GPIO.OUT)    # So setup LEDPin is an output.
# Setup the button.
# As this button is a up and down button, it is currently in a up position.
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# To keep track of what is the state of the button,
# which is the up state, which is True as in it is open right now.
buttonPress = True
ledState = False    # The LED is off right now, so is False.

try:
    while count < blinkCount:       # Which is True
        print("Come on man, press the button!")
        buttonPress = GPIO.input(buttonPin) # GPIO get the buttonPin input.
        if buttonPress == False and ledState == False:
            GPIO.output(LEDPin, True)
            print("LED ON")
            ledState = True
            sleep(3)
        elif buttonPress == False and ledState == True:
            GPIO.output(LEDPin, False)
            print("LED OFF")
            ledState = False
            count += 1
            sleep(0.5)
        sleep(0.1)
finally:
    GPIO.output(LEDPin, False)      # To off everything safely just in case.
    GPIO.cleanup()                  # Reset the GPIO Pins to a safe state.`
