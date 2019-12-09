#! /usr/bin/python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as gpio
import uinput
import time
 
 
gpio.setmode(gpio.BCM)
 
# Com pull-up interno
gpio.setup(12, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(16, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(20, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(21, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(13, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(19, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(26, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(6, gpio.IN, pull_up_down = gpio.PUD_UP)

events = (uinput.KEY_A, uinput.KEY_S, uinput.KEY_D, uinput.KEY_W, uinput.KEY_B, uinput.KEY_X, uinput.KEY_Y, uinput.KEY_Z)
device = uinput.Device(events)
 
while True:
  if gpio.input(12) == gpio.LOW:
    device.emit_click(uinput.KEY_Z)
  if gpio.input(16) == gpio.LOW:
    device.emit_click(uinput.KEY_B)
  if gpio.input(20) == gpio.LOW:
    device.emit_click(uinput.KEY_X)
  if gpio.input(21) == gpio.LOW:
    device.emit_click(uinput.KEY_Y)
  if gpio.input(13) == gpio.LOW:
    device.emit_click(uinput.KEY_A)
  if gpio.input(19) == gpio.LOW:
    device.emit_click(uinput.KEY_S)
  if gpio.input(26) == gpio.LOW:
    device.emit_click(uinput.KEY_D)
  if gpio.input(6) == gpio.LOW:
    device.emit_click(uinput.KEY_W)
  time.sleep(0.1)
 
gpio.cleanup()
exit()
