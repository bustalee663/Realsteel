from robot import robot
from joystick import joystick
from button import button

class user:
    # 4 punch motor pins, 4 move pins, 2 life pins, 1 hit pin, 2 hit pins, 1 punch pin
    def __init__(punchMotorPins, moveMotorPins, lifePins, hitPin, joystickPins, punchPin):
        self.robot = robot(punchMotorPins, moveMotorPins, lifePins, hitPin)
        self.joystick = joystick(joystickPins)
        self.punchButton = button(punchPin)