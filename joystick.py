import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

from button import button

class joystick:
    def __init__(self, buttonPins):
        self.leftButt = button(buttonPins[0])
        self.rightButt = button(buttonPins[1])
        
    def left(self):
        return self.leftButt.pushed()
    
    def right(self):
        return self.rightButt.pushed()