from fancyLED import FancyLED
import board  #pylint: disable=import-error

fancy1 = FancyLED(board.D3,board.D4,board.D5) #LED 1-3
fancy2 = FancyLED(board.D8,board.D9,board.D10)#LED 3-6

while True:             #modules to run through in order
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()
