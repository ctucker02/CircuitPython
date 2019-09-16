import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D10, echo_pin=board.D9)

while True:
    try:
        print((sonar.distance,)
        if distance = 20:
            red = 255
            green = 0
            blue = 0
        if distance < 20:
            red = 255
            green = 0
            blue = 0
        if distance < 5:
            red = 255
            green = 0
            blue = 0

    except RuntimeError:
            print("Retrying!")
            pass
            time.sleep(0.1)