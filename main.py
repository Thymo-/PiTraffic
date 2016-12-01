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
    GPIO.setup(21, GPIO.OUT)

def red(n):
    GPIO.output(n, GPIO.LOw)

# rood(GPIO)
# geel(GPIO)
# groen(GPIO)

setup()
while true:
    GPIO.output(21, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(21, GPIO.LOW)
