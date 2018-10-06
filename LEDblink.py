# Tutorial from youtube link below:
# https://www.youtube.com/watch?v=ntKI2Nj-hSU&list=PLNnwglGGYoTvy37TSGFlv-aFkpg7owWrE&index=22

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount = 3
count = 0
LEDPin = 22     # GPIO22 is where the LED's longer +ve pin is connected to.

# Setup what the GPIO22 is.
GPIO.setup(LEDPin, GPIO.OUT)    # So setup LEDPin as an output.

try:
    while count < blinkCount:       # Which is True
        GPIO.output(LEDPin, True)   # LED blinks On
        print("LED ON")
        sleep(3)                    # Wait for 3 secs with LED ON
        GPIO.output(LEDPin, False)  # LED is Off
        print("LED OFF")
        sleep(1)                    # Wait for 1 sec
        count += 1                  # while loop continue for another 2 round.
finally:
    GPIO.cleanup()                  # Reset the GPIO Pins to a safe state.
