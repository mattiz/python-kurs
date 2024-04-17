# https://learn.adafruit.com/debouncer-library-python-circuitpython-buttons-sensors/overview

import board
import time
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer

btn = DigitalInOut(board.GP14)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
switch = Debouncer(btn)

led = DigitalInOut(board.GP15)
led.direction = Direction.OUTPUT

while True:
    switch.update()

    if switch.rose:
        print('Just released')
        led.value = not led.value

