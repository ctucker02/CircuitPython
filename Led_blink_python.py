import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D3)
led.direction = digitalio.Direction.OUTPUT

while true:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

