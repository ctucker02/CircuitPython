import time
import board
import touchio
import pulseio      #neccessary libraries^
from adafruit_motor import Servo

pwm = pulseio.PWMOut(board.A2, duty_cycle= 2 ** 15, frequency=50) #how long the pulses are and how many there are
my_servo = Servo.Servo(pwm)     #defining servo


touch_A0 = touchio.TouchIn(board.A0)    #making touch pin at A0
touch_A5 = touchio.TouchIn(board.A5)    #making touch pin at A5
my_servo.angle = 0  #start at 0

x = 5
q = 5

while True:
    if touch_A0.value and x>0: #touch value from 0-90
        print('forward')
        my_servo.angle = x  #servo angle = 5
        x = x + q           #when touch_A0 is touched the servo will move 5 degrees forward
        time.sleep(.10)
    if touch_A5.value and x<180: #touch value from 90-180
        print('backward')
        my_servo.angle = x  #servo angle = 5
        x = x - q           #when touch_A5 is touched the servo will move 5 degrees backward
        time.sleep(.10)
