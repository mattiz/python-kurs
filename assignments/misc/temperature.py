# https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/temperature-gauge

import microcontroller
import time

while(True):
    print((microcontroller.cpu.temperature,))  # Open plotter
    time.sleep(0.5)
