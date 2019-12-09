#! /usr/bin/python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as gpio
import uinput
import time
 
 
gpio.setmode(gpio.BCM)
 
# Com pull-up interno
gpio.setup(12, gpio.IN, pull_up_down = gpio.PUD_UP)
 
while True:
  if gpio.input(12) == gpio.LOW:
    print("1")
    with uinput.Device([uinput.KEY_E, uinput.KEY_H, uinput.KEY_L, uinput.KEY_O]) as device:
      device.emit_click(uinput.KEY_E)
  else:
    print("0")
  time.sleep(0.1)
 
gpio.cleanup()
exit()
