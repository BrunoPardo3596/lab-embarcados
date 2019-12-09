#! /usr/bin/python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as gpio
import uinput
import time
 
 
gpio.setmode(gpio.BCM)
 
# Com pull-up interno
gpio.setup(12, gpio.IN, pull_up_down = gpio.PUD_UP)

events = (uinput.KEY_X, uinput.KEY_H, uinput.KEY_E, uinput.KEY_L, uinput.KEY_O)
device = uinput.Device(events)
 
while True:
  if gpio.input(12) == gpio.LOW:
    print("1")
    device.emit(uinput.KEY_X, 1)
  else:
    print("0")
  time.sleep(0.1)
 
gpio.cleanup()
exit()
