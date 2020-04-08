from motor import motor
from lives import lives
from button import button

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class robot:
    # 4 punch motor pins, 4 move pins, 2 life pins, 1 hit pin
    # Will probably make user classes to control robots
    def __init__(self, punchMotorPins, moveMotorPins, lifePins, hitPin):
        self.punchMotor = motor(punchMotorPins)
        self.moveMotor = motor(moveMotorPins)
        self.lives = lives(lifePins)
        self.hitButton = button(hitPin)
    
    # Functions regarding lives
    def update_lives(self):
        self.lives.update()
    
    def get_lives(self):
        return self.lives.count
    
    #Functions regarding being hit
    def is_hit(self):
        return self.hitButton.pushed()
    
    # Functions regarding moving
    def move_left(self):
        self.moveMotor.move_left()
        
    def move_right(self):
        self.moveMotor.move_right()
        
    # Funcitons regarding punching
    def punch(self): # Crude punching of just moving the arm 180 degrees back and forth
        #@TODO update punching
        self.punchMotor.move_left_deg(90)
        self.punchMotor.move_right_deg(90)
        
'''
test = robot([1,2,3,4],[5,6,7,8],[9,10],11)
print(test.is_hit())
print(test.lives.count)
test.lives.update()
print(test.lives.count)
'''