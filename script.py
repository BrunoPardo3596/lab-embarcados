import RPi.GPIO as GPIO
import uinput
import time

buttonUp = 12
buttonDown = 6
buttonRight = 13
buttonLeft = 19
buttonA = 26
buttonB = 21
buttonX = 20
buttonY = 16


def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(buttonUp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonDown, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonLeft, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonRight, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonX, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonY, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def loop():
  while True:
    buttonUpState = GPIO.input(buttonUp)
    buttonDownState = GPIO.input(buttonDown)
    buttonLeftState = GPIO.input(buttonLeft)
    buttonRightState = GPIO.input(buttonRight)
    buttonAState = GPIO.input(buttonA)
    buttonBState = GPIO.input(buttonB)
    buttonXState = GPIO.input(buttonX)
    buttonYState = GPIO.input(buttonY)

    if  buttonUpState == True:
      with uinput.Device([uinput.KEY_UP]) as device:
        device.emit_click(uinput.KEY_UP)
    if  buttonDownState == True:
      with uinput.Device([uinput.KEY_DOWN]) as device:
        device.emit_click(uinput.KEY_DOWN)
    if  buttonLeftState == True:
      with uinput.Device([uinput.KEY_LEFT]) as device:
        device.emit_click(uinput.KEY_LEFT)
    if  buttonRightState == True:
      with uinput.Device([uinput.KEY_RIGHT]) as device:
        device.emit_click(uinput.KEY_RIGHT)
    if  buttonAState == True:
      with uinput.Device([uinput.KEY_A]) as device:
        device.emit_click(uinput.KEY_A)
    if  buttonBState == True:
      with uinput.Device([uinput.KEY_B]) as device:
        device.emit_click(uinput.KEY_B)
    if  buttonXState == True:
      with uinput.Device([uinput.KEY_X]) as device:
        device.emit_click(uinput.KEY_X)
    if  buttonYState == True:
      with uinput.Device([uinput.KEY_Y]) as device:
        device.emit_click(uinput.KEY_Y)

def endprogram():
  GPIO.cleanup()


if __name__ == '__main__':
          
  setup()

  try:
    loop()

  except KeyboardInterrupt:
    print 'keyboard interrupt detected' 
    endprogram()