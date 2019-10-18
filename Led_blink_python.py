import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D3)      #make LED pin
led.direction = digitalio.Direction.OUTPUT

while true:
    led.value = True #LED on
    time.sleep(0.5)
    led.value = False #LED off
    time.sleep(0.5)

