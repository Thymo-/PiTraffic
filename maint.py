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

import time
import RPi.GPIO as GPIO

GPIO_inputs = [26,19,13,6,5,11]
GPIO_outputs = [20,21,12,7,8,25,24,23,18,2,3,4,17,27,22,10,9,14] # Pin 14 not used due to failure.

# Settings
max_timeout = 20 # Maximum amount of time traffic is permitted to wait.
green_time = 6

# Timers
t_now = 0
red1time = 0
red2time = 0
red3time = 0
red4time = 0
red5time = 0
red6time = 0

# States: 0 = Green, 1 = Amber, 2 = Red
state1 = 0
state2 = 0
state3 = 0
state4 = 0
state5 = 0
state6 = 0

def setup():
    GPIO.setmode(GPIO.BCM) # Use BCM chip numbering
    # Define inputs
    GPIO.setup(GPIO_inputs, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # Define outputs
    GPIO.setup(GPIO_outputs, GPIO.OUT)

def sensor_event(channel):
    if GPIO.input(channel):
        print("Input went high: ", channel)

    else:
        print("Input went low: ", channel)

def red(n):
    global state1
    global state2
    global state3
    global state4
    global state5
    global state6
    if n == 1:
        if state1 == 0:
            amber(n)
        elif state1 == 1:
            pass
        else:
            return
        GPIO.output(14, True)
        GPIO.output(20, False)
        GPIO.output(21, False)
        global red1time
        red1time = time.time()
        state1 = 2


    elif n == 2:
        if state2 == 0:
            amber(n)
        elif state2 == 1:
            pass
        else:
            return
        GPIO.output(8, True)
        GPIO.output(7, False)
        GPIO.output(12, False)
        global red2time
        red2time = time.time()
        state2 = 2
        
    elif n == 3:
        if state3 == 0:
            amber(n)
        elif state3 == 1:
            pass
        else:
            return
        GPIO.output(23, True)
        GPIO.output(24, False)
        GPIO.output(25, False)
        global red3time
        red3time = time.time()
        state3 = 2
        
    elif n == 4:
        if state4 == 0:
            amber(n)
        elif state4 == 1:
            pass
        else:
            return
        GPIO.output(2, True)
        GPIO.output(3, False)
        GPIO.output(18, False)
        global red4time
        red4time = time.time()
        state4 = 2
        
    elif n == 5:
        if state5 == 0:
            amber(n)
        elif state5 == 1:
            pass
        else:
            return
        GPIO.output(4, True)
        GPIO.output(17, False)
        GPIO.output(27, False)
        global red5time
        red5time = time.time()
        state5 = 2
        
    elif n == 6:
        if state6 == 0:
            amber(n)
        elif state6 == 1:
            pass
        else:
            return
        GPIO.output(22, True)
        GPIO.output(10, False)
        GPIO.output(9, False)
        global red6time
        red6time = time.time()
        state6 = 2
        
    else:
        print("Invalid identifier!")
    print("Light change: Red ", n)

def amber(n, t=3):
    global state1
    global state2
    global state3
    global state4
    global state5
    global state6
    if n == 1:
        GPIO.output(14, False)
        GPIO.output(20, True)
        GPIO.output(21, False)
        state1 = 1
        time.sleep(t)

    elif n == 2:
        GPIO.output(8, False)
        GPIO.output(7, True)
        GPIO.output(12, False)
        state2 = 1
        time.sleep(t)

    elif n == 3:
        GPIO.output(23, False)
        GPIO.output(24, True)
        GPIO.output(25, False)
        state3 = 1
        time.sleep(t)

    elif n == 4:
        GPIO.output(2, False)
        GPIO.output(3, True)
        GPIO.output(18, False)
        state4 = 1
        time.sleep(t)

    elif n == 5:
        GPIO.output(4, False)
        GPIO.output(17, True)
        GPIO.output(27, False)
        state5 = 1
        time.sleep(t)

    elif n == 6:
        GPIO.output(22, False)
        GPIO.output(10, True)
        GPIO.output(9, False)
        state6 = 1
        time.sleep(t)

    else:
        print("Invalid identifier!")
    print("Light change: Amber ", n)

def green(n):
    global state1
    global state2
    global state3
    global state4
    global state5
    global state6
    if n == 1:
        GPIO.output(14, False)
        GPIO.output(20, False)
        GPIO.output(21, True)
        state1 = 0
    elif n == 2:
        GPIO.output(8, False)
        GPIO.output(7, False)
        GPIO.output(12, True)
        state2 = 0

    elif n == 3:
        GPIO.output(23, False)
        GPIO.output(24, False)
        GPIO.output(25, True)
        state3 = 0

    elif n == 4:
        GPIO.output(2, False)
        GPIO.output(3, False)
        GPIO.output(18, True)
        state4 = 0

    elif n == 5:
        GPIO.output(4, False)
        GPIO.output(17, False)
        GPIO.output(27, True)
        state5 = 0

    elif n == 6:
        GPIO.output(22, False)
        GPIO.output(10, False)
        GPIO.output(9, True)
        state6 = 0

    else:
        print("Invalid identifier!")
    print("Light change: Green ", n)

def off(n, t=3):
    global state1
    global state2
    global state3
    global state4
    global state5
    global state6
    if n == 1:
        GPIO.output(14, False)
        GPIO.output(20, False)
        GPIO.output(21, False)
        state1 = 1
        time.sleep(t)

    elif n == 2:
        GPIO.output(8, False)
        GPIO.output(7, False)
        GPIO.output(12, False)
        state2 = 1
        time.sleep(t)

    elif n == 3:
        GPIO.output(23, False)
        GPIO.output(24, False)
        GPIO.output(25, False)
        state3 = 1
        time.sleep(t)

    elif n == 4:
        GPIO.output(2, False)
        GPIO.output(3, False)
        GPIO.output(18, False)
        state4 = 1
        time.sleep(t)

    elif n == 5:
        GPIO.output(4, False)
        GPIO.output(17, False)
        GPIO.output(27, False)
        state5 = 1
        time.sleep(t)

    elif n == 6:
        GPIO.output(22, False)
        GPIO.output(10, False)
        GPIO.output(9, False)
        state6 = 1
        time.sleep(t)

    else:
        print("Invalid identifier!")
    print("Light change: Off ", n)

def getstate(a):
    if a == 1:
        global state1
        return state1
    elif a == 2:
        global state2
        return state2
    elif a == 3:
        global state3
        return state3
    elif a == 4:
        global state4
        return state4
    elif a == 5:
        global state5
        return state5
    elif a == 6:
        global state6
        return state6

def init(): # Initialization program
    for a in range(1, 7):
        amber(a, 0)
    time.sleep(3)
    for a in range(1, 7):
        red(a)

def makeway(): # Clear junction of traffic
    go_sleep = False
    for a in range(1, 7):
        if getstate(a) == 0:
            amber(a, 0)
            go_sleep = True
    if go_sleep:
        time.sleep(3)
    for a in range(1, 7):
        red(a)
try:
    setup() # Hardware setup
    GPIO.add_event_detect(26, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(19, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(13, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(5, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(11, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    while True: # Main program loop
        for a in range(1, 7):
            amber(a, 0)
        time.sleep(1.1)
        for a in range(1, 7):
            off(a, 0)
        time.sleep(1.1)
        
finally:
    GPIO.cleanup()
