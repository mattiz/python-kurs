# https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-raspberry-pi-pico/adc

import time
import board
import analogio

knob = analogio.AnalogIn(board.A0)

def get_voltage(raw):
    return (raw * 3.3) / 65536

while True:
    raw = knob.value
    volts = get_voltage(raw)
    print("raw = {:5d} volts = {:5.2f}".format(raw, volts))
    time.sleep(0.5)
