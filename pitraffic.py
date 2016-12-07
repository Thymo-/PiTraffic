#!/usr/bin/python
'''
This program is free software: you can redistribute it and/or modify
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

def setup():
    GPIO.setup(GPIO.BCM)
    GPIO.setup(26, GPIO.IN)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    pass

def red(n):
    if n == 1:
        GPIO.output(16, True)
        GPIO.output(20, False)
        GPIO.output(21, False)
    elif n == 2:
        pass
    elif n == 3:
        pass
    else:
        print("Invalid!")
    print("Light change: Red")

def amber(n):
    if n == 1:
        GPIO.output(16, False)
        GPIO.output(20, True)
        GPIO.output(21, False)
    elif n == 2:
        pass
    elif n == 3:
        pass
    else:
        print("Invalid!")
    print("Light change: Amber")

def green(n):
    if n == 1:
        GPIO.output(16, False)
        GPIO.output(20, False)
        GPIO.output(21, True)
    elif n == 2:
        pass
    elif n == 3:
        pass
    else:
        print("Invalid!")
    print("Light change: Green")

setup()
while True:
    red(1)
    time.sleep(3)
    amber(1)
    time.sleep(3)
    green(1)
    time.sleep(3)
