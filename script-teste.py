#! /usr/bin/python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as gpio
import time
 
 
gpio.setmode(gpio.BCM)
 
# Com pull-up interno
gpio.setup(12, gpio.IN, pull_up_down = gpio.PUD_UP)
 
while True:
  if gpio.input(12) == gpio.LOW:
    print("Botão acionado")
  else:
    print("Botão desligado")
  time.sleep(1)
 
gpio.cleanup()
exit()
