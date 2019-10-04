class RGB:

    import time
    import digitalio
    import pulseio

    def __init__(self, red, green, blue):
        self.mred = self.pulseio.PWMOut(red, frequency=5000, duty_cycle=65535)
        self.mgreen = self.pulseio.PWMOut(green, frequency=5000, duty_cycle=65535)
        self.mblue = self.pulseio.PWMOut(blue, frequency=5000, duty_cycle=65535)

    def red(self):
        self.mgreen.duty_cycle = 65535
        self.mblue.duty_cycle = 65535
        self.mred.duty_cycle = 0

    def green(self):
        self.mred.duty_cycle = 65535
        self.mblue.duty_cycle = 65535
        self.mgreen.duty_cycle = 0

    def blue(self):
        self.mgreen.duty_cycle = 65535
        self.mred.duty_cycle = 65535
        self.mblue.duty_cycle = 0

    def cyan(self):
        self.mred.duty_cycle = 65535
        self.mblue.duty_cycle = int(65535*0.5)
        self.mgreen.duty_cycle = int(65535*0.5)  #blue + green = cyan

    def magenta(self):
        self.mgreen.duty_cycle = 65535
        self.mred.duty_cycle = int(65535*0.5)
        self.mblue.duty_cycle = int(65535*0.5) #red + blue = magenta

    def yellow(self):
        self.mblue.duty_cycle = 65535
        self.mred.duty_cycle = int(65535*0.5)
        self.mgreen.duty_cycle = int(65535*0.5) #red + green = yellow