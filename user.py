from robot import robot

class user:
    def __init__(punchMotorPins, moveMotorPins, lifePins, hitPin, joystickPins, punchPin):
        self.robot = robot(punchMotorPins, moveMotorPins, lifePins, hitPin)
        self.joystick = joystick(joystickPins)
        self.punchButton = button(punchPin)
        # @TODO Do I need to add the rail bumpers or will that be taken care of in hardware?