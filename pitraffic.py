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
GPIO_outputs = [20,21,12,7,8,25,24,23,18,2,3,4,17,27,22,10,9,14] # Pin 14 not used due to hardware failure on my board.

# Settings
max_timeout = 20    # Maximum amount of time traffic is permitted to wait.
green_time = 8      # Initial time a light is green.
amber_time = 3      # Time a light stays amber before going red.
extend = 3          # Time green light is extended by if cars still present
max_iteration = 3   # Maximum amount of times green light is extended

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

# Sensor states: 0 = Free, 1 = Occupied
sense1 = True
sense2 = False
sense3 = False
sense4 = False
sense5 = False
sense6 = False

def setup():
    GPIO.setmode(GPIO.BCM) # Use BCM chip numbering
    # Define inputs
    GPIO.setup(GPIO_inputs, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # Define outputs
    GPIO.setup(GPIO_outputs, GPIO.OUT)
    # Setup event listeners
    GPIO.add_event_detect(26, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(19, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(13, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(5, GPIO.BOTH, callback=sensor_event, bouncetime=1000)
    GPIO.add_event_detect(11, GPIO.BOTH, callback=sensor_event, bouncetime=1000)

def sensor_event(channel):
    global sense1
    global sense2
    global sense3
    global sense4
    global sense5
    global sense6
    if GPIO.input(channel): # Sensor high
        if channel == 26:
            sense1 = True
        elif channel == 19:
            sense2 = True
        elif channel == 13:
            sense3 = True
        elif channel == 6:
            sense4 = True
        elif channel == 5:
            sense5 = True
        elif channel == 11:
            sense6 = True
        print("Input went high: ", channel)
    else: # Sensor low
        if channel == 26:
            sense1 = False
        elif channel == 19:
            sense2 = False
        elif channel == 13:
            sense3 = False
        elif channel == 6:
            sense4 = False
        elif channel == 5:
            sense5 = False
        elif channel == 11:
            sense6 = False
        print("Input went low: ", channel)

def priority():
    makeway()
    for i in range(1, 7):
        if i == 1:
            green(1)
            green(3)
            green(5)
            time.sleep(green_time)
            iteration = 0
            while (sense1 or sense3 or sense5) and iteration < max_iteration and limit():
                time.sleep(extend)
                iteration += 1
            amber(1, 0)
            amber(3, 0)
            amber(5, 0)
            time.sleep(amber_time)
            red(1, 0)
            red(3, 0)
            red(5, 0)
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

def limit():
    t_now = time.time()
    if (t_now - red1time) >= max_timeout:
        makeway()
        green(1)
        time.sleep(green_time)
        makeway()
        return False

    if (t_now - red2time) >= max_timeout:
        makeway()
        green(2)
        time.sleep(green_time)
        makeway()
        return False
    
    if (t_now - red3time) >= max_timeout:
        makeway()
        green(3)
        time.sleep(green_time)
        makeway()
        return False

    if (t_now - red4time) >= max_timeout:
        makeway()
        green(4)
        time.sleep(green_time)
        makeway()
        return False
    
    if (t_now - red5time) >= max_timeout:
        makeway()
        green(5)
        time.sleep(green_time)
        makeway()
        return False
    
    if (t_now - red6time) >= max_timeout:
        makeway()
        green(6)
        time.sleep(green_time)
        makeway()
        return False
    return True
    
def red(n, t=3):
    global state1
    global state2
    global state3
    global state4
    global state5
    global state6
    if n == 1:
        if state1 == 0:
            amber(n, t)
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
            amber(n, t)
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
            amber(n, t)
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
            amber(n, t)
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
            amber(n, t)
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
            amber(n, t)
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
        off(a, 0)
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
    time.sleep(2)

try:
    setup() # Hardware setup
    init() # Go into service
    while True: # Main program loop
        limit()
        priority()
        time.sleep(0.5)
        
finally:
    GPIO.cleanup()
