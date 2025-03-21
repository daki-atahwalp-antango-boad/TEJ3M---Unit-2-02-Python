# This program turns the LED on the pico on and off, increasing the time the light stays on each cycle by one second
#
# Created by: Daki A.B
# Created on: Mar 2025
import time
import board
import digitalio

# variables
blink_time = 1

# setting LED pin to output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# running loop, turning LED on for one second and for one second, increases every cycle by one second
while True:
    led.value = True
    time.sleep(blink_time)
    led.value = False
    time.sleep(blink_time)
    blink_time += 1
