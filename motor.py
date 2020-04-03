import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class motor:
    def __init__(self, pins):
        self.P1 = pins[0]
        self.P2 = pins[1]
        self.P3 = pins[2]
        self.P4 = pins[3]
        GPIO.setup(self.P1, GPIO.OUT)
        GPIO.setup(self.P2, GPIO.OUT)
        GPIO.setup(self.P3, GPIO.OUT)
        GPIO.setup(self.P4, GPIO.OUT)
        self.sleepTime = 0.001 # Adjust this for differing speeds
        
    def move_left(self): # Left & right may switch
        GPIO.output(self.P3, 0)
        time.sleep(self.sleepTime)
        GPIO.output(self.P1, 1)
        time.sleep(self.sleepTime)
        GPIO.output(self.P4, 0)
        time.sleep(self.sleepTime)
        GPIO.output(self.P2, 1)
        time.sleep(self.sleepTime)
        GPIO.output(self.P1, 0)
        time.sleep(self.sleepTime)
        GPIO.output(self.P3, 1)
        time.sleep(self.sleepTime)
        GPIO.output(self.P2, 0)
        time.sleep(self.sleepTime)
        GPIO.output(self.P4, 1)
        time.sleep(self.sleepTime)
        
    def move_right(self): # Left & right may switch
        GPIO.output(self.P1, 0)
        time.sleep(self.sleepTime)
        GPIO.output(self.P3, 1)
        time.sleep(self.sleepTime)
        GPIO.output(self.P4, 0)
        time.sleep(self.sleepTime)
        GPIO.output(self.P2, 1)
        time.sleep(self.sleepTime)
        GPIO.output(self.P3, 0)
        time.sleep(self.sleepTime)
        GPIO.output(self.P1, 1)
        time.sleep(self.sleepTime)
        GPIO.output(self.P2, 0)
        time.sleep(self.sleepTime)
        GPIO.output(self.P4, 1)
        time.sleep(self.sleepTime)
        
    def move_left_deg(self, degrees): # Left & right may switch
        for _ in range(0, int(degrees*512/360)):
            GPIO.output(self.P3, 0)
            time.sleep(self.sleepTime)
            GPIO.output(self.P1, 1)
            time.sleep(self.sleepTime)
            GPIO.output(self.P4, 0)
            time.sleep(self.sleepTime)
            GPIO.output(self.P2, 1)
            time.sleep(self.sleepTime)
            GPIO.output(self.P1, 0)
            time.sleep(self.sleepTime)
            GPIO.output(self.P3, 1)
            time.sleep(self.sleepTime)
            GPIO.output(self.P2, 0)
            time.sleep(self.sleepTime)
            GPIO.output(self.P4, 1)
            time.sleep(self.sleepTime)
            
    def move_right_deg(self, degrees): # Left & right may switch
        for _ in range(0, int(degrees*512/360)):
            GPIO.output(self.P1, 0)
            time.sleep(self.sleepTime)
            GPIO.output(self.P3, 1)
            time.sleep(self.sleepTime)
            GPIO.output(self.P4, 0)
            time.sleep(self.sleepTime)
            GPIO.output(self.P2, 1)
            time.sleep(self.sleepTime)
            GPIO.output(self.P3, 0)
            time.sleep(self.sleepTime)
            GPIO.output(self.P1, 1)
            time.sleep(self.sleepTime)
            GPIO.output(self.P2, 0)
            time.sleep(self.sleepTime)
            GPIO.output(self.P4, 1)
            time.sleep(self.sleepTime)
