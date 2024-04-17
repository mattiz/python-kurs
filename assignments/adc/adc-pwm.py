# https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-raspberry-pi-pico/pwm

import board
import pwmio
import analogio
import time

knob = analogio.AnalogIn(board.A0)

led = pwmio.PWMOut(board.GP15, frequency=1000)

while True:
    led.duty_cycle = knob.value
    print((led.duty_cycle,))  # Open plotter
    time.sleep(0.05)
