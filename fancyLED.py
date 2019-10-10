import board  #pylint: disable=import-error
import time  #pylint: disable=import-error
from digitalio import DigitalInOut, Direction, Pull  #pylint: disable=import-error

class FancyLED(object):
    def __init__(self, pin1, pin2, pin3):
        self.pin1 = DigitalInOut(pin1)
        self.pin1.direction = Direction.OUTPUT
        self.pin2 = DigitalInOut(pin2)
        self.pin2.direction = Direction.OUTPUT
        self.pin3 = DigitalInOut(pin3)
        self.pin3.direction = Direction.OUTPUT

    def alternate(self):
        self.pin1.value = True
        self.pin2.value = False
        self.pin3.value = True
        time.sleep(0.5)
        self.pin1.value = False
        self.pin2.value = True
        self.pin3.value = False
        time.sleep(0.5)
        print("working")
        
    def chase(self):
        self.pin3.value = False
        self.pin1.value = True
        time.sleep(0.5)
        self.pin1.value = False
        self.pin2.value = True
        time.sleep(0.5)
        self.pin2.value = False
        self.pin3.value = True
        time.sleep(0.5)

    def blink(self):
        self.pin1.value = True
        self.pin2.value = True
        self.pin3.value = True
        time.sleep(0.5)
        self.pin1.value = False
        self.pin2.value = False
        self.pin3.value = False
        time.sleep(0.5)

    def sparkle(self):
        self.pin1.value = True
        time.sleep(0.01)
        self.pin1.value = False
        time.sleep(0.01)
        self.pin2.value = True
        time.sleep(0.01)
        self.pin2.value = False
        time.sleep(0.01)
        self.pin3.value = True
        time.sleep(0.01)
        self.pin3.value = False
        time.sleep(0.01)
        self.pin3.value = False
        self.pin3.value = False
        self.pin1.value = False
        self.pin2.value = False
        self.pin3.value = False