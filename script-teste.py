#! /usr/bin/python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as gpio
import time
 
 
gpio.setmode(gpio.BCM)
 
# Com pull-up interno
gpio.setup(12, gpio.IN, pull_up_down = gpio.PUD_UP)
 
while True:
  if gpio.input(12) == gpio.LOW:
    print("1")
  else:
    print("0")
 
gpio.cleanup()
exit()
