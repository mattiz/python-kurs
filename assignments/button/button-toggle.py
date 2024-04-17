import board
import time
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.GP14)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

led = DigitalInOut(board.GP15)
led.direction = Direction.OUTPUT

prev_state = btn.value

while True:
    cur_state = btn.value
    if cur_state != prev_state:
        if cur_state:
            print("BTN is pressed")
            led.value = not led.value

    prev_state = cur_state
    time.sleep(0.1) # Sleep for debounce

