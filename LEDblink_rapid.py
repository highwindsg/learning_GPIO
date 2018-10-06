#https://www.youtube.com/watch?v=ZNNpoLFbL9E&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=61

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)     # Red LED
GPIO.setup(17, GPIO.OUT)    # Yellow LED
GPIO.setup(22, GPIO.OUT)    # Green LED
GPIO.setup(5, GPIO.OUT)     # Blue LED

try:
    while True:
        GPIO.output(4, True)    # Turn on red LED
        time.sleep(1)           # Wait for 5 secs
        GPIO.output(4, False)   # Turn off red LED

        GPIO.output(17, True)   # Turn on yellow LED
        time.sleep(1)           # Wait for 5 secs
        GPIO.output(17, False)  # Turn off yellow LED

        GPIO.output(22, True)   # Turn on green LED
        time.sleep(1)           # Wait for 5 secs
        GPIO.output(22, False)  # Turn off yellow LED

        GPIO.output(5, True)    # Turn on blue LED
        time.sleep(1)           # Wait for 5 secs
        GPIO.output(5, False)   # Turn off blue LED
finally:
    GPIO.output(4, False)       # To turn off LED just in case
    GPIO.output(17, False)      # To turn off LED just in case
    GPIO.output(22, False)      # To turn off LED just in case
    GPIO.output(5, False)       # To turn off LED just in case
    GPIO.cleanup()              # Reset the GPIO Pins to a safe state
