from microbit import *
import time

positions = [2, 2, 2, 2, 2]

def scroll_up():
    for y in range(4):
        positions[y] = positions[y + 1]

while True:
    display.clear()
    scroll_up()
    positions[4] = int(pin2.read_analog() / 240)
    for y2 in range(5):
        display.set_pixel(positions[y2], y2, 9)
    time.sleep(0.1)
