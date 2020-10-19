from microbit import *
import time

while True:
    data = (pin2.read_analog(),)
    print(data)
    time.sleep(0.05)
