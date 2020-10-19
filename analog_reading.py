from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll(pin2.read_analog())
