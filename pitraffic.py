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

def setup():
    GPIO.setup(GPIO.BCM) # Use BCM chip numbering
    # Define inputs
    GPIO.setup(26, GPIO.IN)
    GPIO.setup(19, GPIO.IN)
    GPIO.setup(13, GPIO.IN)
    GPIO.setup(6, GPIO.IN)
    GPIO.setup(5, GPIO.IN)
    GPIO.setup(11, GPIO.IN)
    # Define outputs
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)

def sensor_loop():
    pass

def red(n):
    if n == 1:
        GPIO.output(16, True)
        GPIO.output(20, False)
        GPIO.output(21, False)
        light1 = 0  
    elif n == 2:
        pass
    elif n == 3:
        pass
    else:
        print("Invalid!")
    print("Light change: Red ", n)

def amber(n):
    if n == 1:
        GPIO.output(16, False)
        GPIO.output(20, True)
        GPIO.output(21, False)
        light1 = 1
    elif n == 2:
        pass
    elif n == 3:
        pass
    else:
        print("Invalid!")
    print("Light change: Amber ", n)

def green(n):
    if n == 1:
        GPIO.output(16, False)
        GPIO.output(20, False)
        GPIO.output(21, True)
        light1 = "green"
    elif n == 2:
        pass
    elif n == 3:
        pass
    else:
        print("Invalid!")
    print("Light change: Green ", n)

setup()
while True:
    red(1)
    sleep(3)
    amber(1)
    sleep(3)
    green(1)
    sleep(3)
GPIO.cleanup()
