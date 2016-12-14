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
import RPi.GPIO as GPIO

GPIO_inputs = [26,19,13,6,5,11]
GPIO_outputs = [16,20,21,12,7,8,25,24,23,18,2,3,4,17,27,22,10,9]

def setup():
    GPIO.setmode(GPIO.BCM) # Use BCM chip numbering
    # Define inputs
    GPIO.setup(GPIO_inputs, GPIO.IN)
    # Define outputs
    GPIO.setup(GPIO_outputs, GPIO.OUT)

def sensor_loop():
    pass

def red(n):
    if n == 1:
        GPIO.output(16, True)
        GPIO.output(20, False)
        GPIO.output(21, False)
    elif n == 2:
        GPIO.output(8, True)
        GPIO.output(7, False)
        GPIO.output(12, False)
    elif n == 3:
        GPIO.output(23, True)
        GPIO.output(24, False)
        GPIO.output(25, False)
    elif n == 4:
        GPIO.output(2, True)
        GPIO.output(3, False)
        GPIO.output(18, False)
    elif n == 5:
        GPIO.output(4, True)
        GPIO.output(17, False)
        GPIO.output(27, False)
    elif n == 6:
        GPIO.output(22, True)
        GPIO.output(10, False)
        GPIO.output(9, False)
    else:
        print("Invalid identifier!")
    print("Light change: Red ", n)

def amber(n):
    if n == 1:
        GPIO.output(16, False)
        GPIO.output(20, True)
        GPIO.output(21, False)
    elif n == 2:
        GPIO.output(8, False)
        GPIO.output(7, True)
        GPIO.output(12, False)
    elif n == 3:
        GPIO.output(23, False)
        GPIO.output(24, True)
        GPIO.output(25, False)
    elif n == 4:
        GPIO.output(2, False)
        GPIO.output(3, True)
        GPIO.output(18, False)
    elif n == 5:
        GPIO.output(4, False)
        GPIO.output(17, True)
        GPIO.output(27, False)
    elif n == 6:
        GPIO.output(22, False)
        GPIO.output(10, True)
        GPIO.output(9, False)
    else:
        print("Invalid identifier!")
    print("Light change: Amber ", n)

def green(n):
    if n == 1:
        GPIO.output(16, False)
        GPIO.output(20, False)
        GPIO.output(21, True)
    elif n == 2:
        GPIO.output(8, False)
        GPIO.output(7, False)
        GPIO.output(12, True)
    elif n == 3:
        GPIO.output(23, False)
        GPIO.output(24, False)
        GPIO.output(25, True)
    elif n == 4:
        GPIO.output(2, False)
        GPIO.output(3, False)
        GPIO.output(18, True)
    elif n == 5:
        GPIO.output(4, False)
        GPIO.output(17, False)
        GPIO.output(27, True)
    elif n == 6:
        GPIO.output(22, False)
        GPIO.output(10, False)
        GPIO.output(9, True)
    else:
        print("Invalid identifier!")
    print("Light change: Green ", n)

try:
    setup()
    while True:
        red(1)
        red(2)
        red(3)
        red(4)
        red(5)
        red(6)
        sleep(3)
        amber(1)
        amber(2)
        amber(3)
        amber(4)
        amber(5)
        amber(6)
        sleep(3)
        green(1)
        green(2)
        green(3)
        green(4)
        green(5)
        green(6)
        sleep(3)
finally:
    GPIO.cleanup()
