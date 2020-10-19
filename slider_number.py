from microbit import *

while True:
    x = int(pin2.read_analog() / 110)
    display.show(x)


