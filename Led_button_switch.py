import time
import board
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode

lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
button = DigitalInOut(board.D2)     #make button pin
button.direction = Direction.INPUT  
button.pull = Pull.UP               #give power to button
switch = DigitalInOut(board.D5)     #make switch pin
switch.direction = Direction.INPUT
switch.pull = Pull.UP               #give power to switch
lcd.set_cursor_mode(CursorMode.LINE)

press = False #press starts at false until proven otherwise
x = 0       #starts at 0

while True:
    print(button.value)
    lcd.backlight = True       #backlight is on
    if not button.value:
        if (press == False):
            press = True   #if press does not equal false then press equals true
            if not switch.value:
                x = x -1        #if it does not equal switch value then it goes down by one
            if switch.value:
                x = x +1        #if it does equal switch value then it goes up by one
        print((0,))
    if button.value:
        press = False           #these print and display when it is false, which it is set to
    lcd.set_cursor_pos(0, 0)    #sets cursor to start of LCD screen in the first row (0,0)
    lcd.print("Presses: ")
    lcd.set_cursor_pos(0, 10)   #sets cursor to the end of LCD screen in the first row (0,10)
    lcd.print ( str (x))
    lcd.print ("    ")
    lcd.set_cursor_pos(1, 0)    #sets cursor to the start of LCD screen in the second row (1,0)
    lcd.print ("Switch:  ")
    if not switch.value:
        lcd.print ("DOWN")
    if switch.value:
        lcd.print ("UP  ")      #when switch is on value goes up, when it is off then value goes down
    time.sleep(0.05)
