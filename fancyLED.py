import board  #pylint: disable=import-error
import time  #pylint: disable=import-error
from digitalio import DigitalInOut, Direction, Pull  #pylint: disable=import-error

class FancyLED(object):
    def __init__(self, pin1, pin2, pin3):   #defining LED pins
        self.pin1 = DigitalInOut(pin1)
        self.pin1.direction = Direction.OUTPUT
        self.pin2 = DigitalInOut(pin2)
        self.pin2.direction = Direction.OUTPUT
        self.pin3 = DigitalInOut(pin3)
        self.pin3.direction = Direction.OUTPUT

    def alternate(self):
        for stuff in range(0,3):  #repeat code below 3 times
            stuff = stuff
            self.pin1.value = True
            self.pin2.value = False     #creating alternating pattern by the LED being off or on
            self.pin3.value = True
            time.sleep(0.5)
            self.pin1.value = False
            self.pin2.value = True
            self.pin3.value = False
            time.sleep(0.5)
            self.pin1.value = False
            self.pin2.value = False
            self.pin3.value = False
            print("working")

    def chase(self):
        for stuff in range(0,3):    #repeat code below 3 times
            stuff = stuff
            self.pin3.value = False
            self.pin1.value = True
            time.sleep(0.5)
            self.pin1.value = False
            self.pin2.value = True
            time.sleep(0.5)
            self.pin2.value = False
            self.pin3.value = True
            time.sleep(0.5)         #code above makes one led turn off as the next turns on making it "chase" itself
        self.pin1.value = False
        self.pin2.value = False
        self.pin3.value = False

    def blink(self):
        for stuff in range(0,3):    #repeat code below 3 times
            stuff = stuff
            self.pin1.value = True
            self.pin2.value = True
            self.pin3.value = True
            time.sleep(0.5)
            self.pin1.value = False
            self.pin2.value = False
            self.pin3.value = False
            time.sleep(0.5)             #code above makes the LEDs blink on and off together

    def sparkle(self):
        for stuff in range(0,10):   #repeat code below 10 times
            stuff = stuff
            self.pin1.value = True
            time.sleep(0.025)
            self.pin1.value = False
            time.sleep(0.025)
            self.pin2.value = True
            time.sleep(0.025)
            self.pin2.value = False
            time.sleep(0.025)
            self.pin3.value = True
            time.sleep(0.025)
            self.pin3.value = False
            time.sleep(0.025)
            self.pin3.value = True
            time.sleep(0.025)
            self.pin1.value = True
            time.sleep(0.025)
            self.pin2.value = True
            time.sleep(0.025)
            self.pin3.value = True      #code above makes the LEDs flash fastly making it "sparkle"
        self.pin1.value = False
        self.pin2.value = False
        self.pin3.value = False         
        time.sleep(2)                   #sets back all off so it can have a clear start
