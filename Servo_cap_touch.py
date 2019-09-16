import time
import board
import touchio
import pulseio
from adafruit_motor import Servo

pwm = pulseio.PWMOut(board.A2, duty_cycle= 2 ** 15, frequency=50)
my_servo = Servo.Servo(pwm)


touch_A0 = touchio.TouchIn(board.A0)
touch_A5 = touchio.TouchIn(board.A5)
my_servo.angle = 0

x = 5
q = 5

while True:
    if touch_A0.value and x>0:
        print('forward')
        my_servo.angle = x
        x = x + q
        time.sleep(.10)
    if touch_A5.value and x<180:
        print('backward')
        my_servo.angle = x
        x = x - q
        time.sleep(.10)
