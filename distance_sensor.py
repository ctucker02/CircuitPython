import time
import board
import neopixel     #necessary libraries
from adafruit_hcsr04 import HCSR04  

trig = board.D9     
echo = board.D10    #where the sensor is plugged into
sonar = HCSR04(trig, echo)      
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
red = 225   #starts at 225
green = 0   #starts at 0
blue = 0    #starts at 0

distance = 0 #distance variable starts at 0

while True:
    dot.fill((red, green, blue))
    if distance<=20:            #distance is less than or equal to 20
       red = 255-(12*distance)  #red decreases by increments of 12 based on the distance
       blue = 0+(12*distance)   #blue increases by increments of 12 based on the distance
       green = 0                #green stays the same
    elif distance >20:                  #distance is greater than or equal to 20
        green = 0+(12*(distance-20))    #green increases by increments of 12 based on the distance-20
        blue = 225-(12*(distance-20))   #blue decreases by increments of 12 based on the distance-20
        red = 0                         #red stays the same
    if red<=0:
        red =0
    if blue >=225:
        blue =225
    if blue <=0:
        blue = 0
    if green >=225:
        green = 225

    try:
        print (int(sonar.distance))
        distance = (int(sonar.distance))
    except RuntimeError:                    
        pass                #code won't stop if you are too far away because runtime error is passed
    time.sleep(0.05)
