import time
import board        #these libraries are needed
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface


lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)  
PI = DigitalInOut(board.D5)
PI.direction = Direction.INPUT  #making photointerrupter pin and declaring as DigitalInOut object
PI.pull = Pull.UP


x = 0   #Set at zero until proven otherwise

interrupt = False
while True:
    #print(PI.value)
    lcd.backlight = True
    if PI.value:        
        if interrupt == False:
            interrupt = True        #if interrupt isn't false then it is true
            x = x + 1       #count up by one if PI value 
    if not PI.value:
        interrupt = False   #if not PI value then it is back to starting x=0
        x = x

    #print(("Interrupted"))
    if time.monotonic () % 4 == 0:
        lcd.set_cursor_pos(0, 0)
        lcd.print("Interrupted: ")
        lcd.set_cursor_pos(0, 12)
        lcd.print ( str (x))
        lcd.set_cursor_pos(1, 0)
        lcd.print ("Times")
