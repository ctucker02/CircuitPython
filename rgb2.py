import time
import board
from rgb import RGB   # import the RGB class from the rgb module

r1 = board.D10
g1 = board.D9
b1 = board.D8
r2 = board.D4           #defining color pins
g2 = board.D3
b2 = board.D5

myRGB1 = RGB(r1,g1,b1)   # create a new RGB object
myRGB2 = RGB(r2,g2,b2)  

while True:             #colors to run through in order
        myRGB1.red()
        myRGB2.green()
        time.sleep(1)
        myRGB1.blue()
        myRGB2.cyan()
        time.sleep(1)
        myRGB1.magenta()
        myRGB2.yellow()
        time.sleep(1)
