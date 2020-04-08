from led import LED

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class lives:
    def __init__(self, ledPins):
        self.led1 = LED(ledPins[0])
        self.led2 = LED(ledPins[1])
        self.count = 3 # The default
        self.led1.on()
        self.led2.on()
        
    def update(self):
        if self.count >= 1:
            self.count = self.count - 1
        if (self.count == 3):
            self.led1.on()
            self.led2.on()
        elif(self.count == 2):
            self.led1.on()
            self.led2.off()
        elif(self.count == 1):
            self.led1.off()
            self.led2.off()
        elif(self.count == 0):
            self.led1.off()
            self.led2.off()
            
    def reset(self):
        self.count = 3
        self.led1.on()
        self.led2.on()
        
            # Coordinate with the robots if the lives.count == 0 then game over