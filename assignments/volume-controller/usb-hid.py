import usb_hid
import time
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

consumer = ConsumerControl(usb_hid.devices)

while True:
    consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
    time.sleep(1)
    #consumer.send(ConsumerControlCode.VOLUME_DECREMENT)

