import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class LED: # Each LED will have either on or off
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
    
    def on(self):
        GPIO.output(self.pin, 1)
        
    def off(self):
        GPIO.output(self.pin, 0)