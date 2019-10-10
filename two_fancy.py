from fancyLED import FancyLED

fancy1 = FancyLED(3,4,5)
fancy2 = FancyLED(8,9,10)

while True:
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()