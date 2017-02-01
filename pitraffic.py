#!/usr/bin/python
'''This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''

from time import sleep
from collections import deque
import RPi.GPIO as GPIO

GPIO_inputs = [26,19,13,6,5,11]
GPIO_outputs = [16,20,21,12,7,8,25,24,23,18,2,3,4,17,27,22,10,9]
queue = deque([])
red_state = []
amber_state = [1,2,3,4,5,6]
green_state = []

def setup():
    GPIO.setmode(GPIO.BCM) # Use BCM chip numbering
    # Define inputs
    GPIO.setup(GPIO_inputs, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # Define outputs
    GPIO.setup(GPIO_outputs, GPIO.OUT)

def sensor_event(channel):
    if GPIO.input(channel):
        print("Input went high: ", channel)
        queue.insert(channel) # kijken als hij al instaat!
    else:
        print("Input went low: ", channel)
        #queue. Weghalen?

def priority(i):
    if i == 1:
        
    elif i == 2:
        pass
    elif i == 3:
        pass
    elif i == 4:
        pass
    elif i == 5:
        pass
    elif i == 6:
        pass

def red(n):
    if n == 1:
        GPIO.output(16, True)
        GPIO.output(20, False)
        GPIO.output(21, False)
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        red_state.remove(red_state.remove(n)
        red_state.append(n)

    elif n == 2:
        GPIO.output(8, True)
        GPIO.output(7, False)
        GPIO.output(12, False)
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        red_state.remove(red_state.remove(n)
        red_state.append(n)
        
    elif n == 3:
        GPIO.output(23, True)
        GPIO.output(24, False)
        GPIO.output(25, False)
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        red_state.remove(red_state.remove(n)
        red_state.append(n)
        
    elif n == 4:
        GPIO.output(2, True)
        GPIO.output(3, False)
        GPIO.output(18, False)
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        red_state.remove(red_state.remove(n)
        red_state.append(n)
        
    elif n == 5:
        GPIO.output(4, True)
        GPIO.output(17, False)
        GPIO.output(27, False)
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        red_state.remove(red_state.remove(n)
        red_state.append(n)
        
    elif n == 6:
        GPIO.output(22, True)
        GPIO.output(10, False)
        GPIO.output(9, False)
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        red_state.remove(red_state.remove(n)
        red_state.append(n)
        
    else:
        print("Invalid identifier!")
    print("Light change: Red ", n)

def amber(n):
    if n == 1:
        GPIO.output(16, False)
        GPIO.output(20, True)
        GPIO.output(21, False)
        red_state.remove(red_state.index(n))
        green_state.remove(green_state.index(n))
        amber_state.remove(amber_state.index(n))
        amber_state.append(n)

    elif n == 2:
        GPIO.output(8, False)
        GPIO.output(7, True)
        GPIO.output(12, False)
        red_state.remove(red_state.index(n))
        green_state.remove(green_state.index(n))
        amber_state.remove(amber_state.index(n))
        amber_state.append(n)

    elif n == 3:
        GPIO.output(23, False)
        GPIO.output(24, True)
        GPIO.output(25, False)
        red_state.remove(red_state.index(n))
        green_state.remove(green_state.index(n))
        amber_state.remove(amber_state.index(n))
        amber_state.append(n)

    elif n == 4:
        GPIO.output(2, False)
        GPIO.output(3, True)
        GPIO.output(18, False)
        red_state.remove(red_state.index(n))
        green_state.remove(green_state.index(n))
        amber_state.remove(amber_state.index(n))
        amber_state.append(n)

    elif n == 5:
        GPIO.output(4, False)
        GPIO.output(17, True)
        GPIO.output(27, False)
        red_state.remove(red_state.index(n))
        green_state.remove(green_state.index(n))
        amber_state.remove(amber_state.index(n))
        amber_state.append(n)

    elif n == 6:
        GPIO.output(22, False)
        GPIO.output(10, True)
        GPIO.output(9, False)
        red_state.remove(red_state.index(n))
        green_state.remove(green_state.index(n))
        amber_state.remove(amber_state.index(n))
        amber_state.append(n)

    else:
        print("Invalid identifier!")
    print("Light change: Amber ", n)

def green(n):
    if n == 1:
        GPIO.output(16, False)
        GPIO.output(20, False)
        GPIO.output(21, True)
        red_state.remove(red_state.index(n))
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        green_state.append(n)

    elif n == 2:
        GPIO.output(8, False)
        GPIO.output(7, False)
        GPIO.output(12, True)
        red_state.remove(red_state.index(n))
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        green_state.append(n)

    elif n == 3:
        GPIO.output(23, False)
        GPIO.output(24, False)
        GPIO.output(25, True)
        red_state.remove(red_state.index(n))
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        green_state.append(n)

    elif n == 4:
        GPIO.output(2, False)
        GPIO.output(3, False)
        GPIO.output(18, True)
        red_state.remove(red_state.index(n))
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        green_state.append(n)

    elif n == 5:
        GPIO.output(4, False)
        GPIO.output(17, False)
        GPIO.output(27, True)
        red_state.remove(red_state.index(n))
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        green_state.append(n)

    elif n == 6:
        GPIO.output(22, False)
        GPIO.output(10, False)
        GPIO.output(9, True)
        red_state.remove(red_state.index(n))
        amber_state.remove(amber_state.index(n))
        green_state.remove(green_state.index(n))
        green_state.append(n)

    else:
        print("Invalid identifier!")
    print("Light change: Green ", n)

try:
    setup()
    GPIO.add_event_detect(26, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(19, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(13, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(5, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(11, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    while True: # Main program loop
        
        
    while True:
        sleep(1)
finally:
    GPIO.cleanup()
