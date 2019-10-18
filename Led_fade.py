import time
import board    #these libraries are needed
import pulseio

led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0) #PMW output at D13

while True:
    for i in range(100):       #i in range from 0-100

        if i < 50:
            led.duty_cycle = int(i * 2 * 65535 / 100) #fading up by 65535 / 100
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100) #fading down * 65535 / 100
        time.sleep(0.01)







