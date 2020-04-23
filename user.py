from time import sleep
from robot import robot
from joystick import joystick
from button import button

class user:
    # 4 punch motor pins, 4 move pins, 2 life pins, 1 hit pin, 2 hit pins, 1 punch pin
    def __init__(self, punchMotorPins, moveMotorPins, lifePins, hitPin, joystickPins, punchPin):
        self.robot = robot(punchMotorPins, moveMotorPins, lifePins, hitPin)
        self.joystick = joystick(joystickPins)
        self.punchButton = button(punchPin)
        self.victory = False
    
    def get_lives(self):
        return self.robot.get_lives()
    
    def move(self):
        if self.joystick.left():
            self.robot.move_left()
        elif self.joystick.right():
            self.robot.move_right()
        
    def punch(self):
            if self.punchButton.pushed():
                self.robot.punch()
        
    def is_hit(self):
        if self.robot.is_hit():
            self.robot.update_lives()
            sleep(0.5)
                
    def user_input(self):
        if not self.victory:
            self.punch()
            self.move()
            self.is_hit()
            sleep(0.001)
    
'''
    def move_left(self):
        self.robot.move_left()
        
    def move_right(self):
        self.robot.move_left()
        
    def punch(self):
        self.robot.punch()
        
    def is_hit():
        self.robot.is_hit()
        
    def update_lives(self):
        self.robot.update_lives()
'''   