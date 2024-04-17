# https://learn.adafruit.com/circuitpython-essentials/circuitpython-pwm

import time
import board
import pwmio

led = pwmio.PWMOut(board.GP15, frequency=5000, duty_cycle=0)

while True:
    for i in range(100):
        if i < 50:
            led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        
        print((led.duty_cycle,))  # Open plotter
        time.sleep(0.02)

