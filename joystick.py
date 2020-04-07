import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

from button import button

class joystick:
    def __init__(self, buttonPins):
        self.left = button(buttonPins[0])
        self.right = button(buttonPins[1])
        GPIO.setup(self.left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
    def left(self):
        return (GPIO.input(self.right) == 0 and GPIO.input(self.left) == 1)
    
    def right(self):
        return (GPIO.input(self.right) == 1 and GPIO.input(self.left) == 0)