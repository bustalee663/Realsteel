from time import sleep
from user import user
from robot import robot
from led import LED
from lives import lives
from joystick import joystick
from motor import motor
from button import button

# 4 punch motor pins, 4 move pins, 2 life pins, 1 hit pin, 2 joy pins, 1 punch pin

punchButton = button(16)
hitButton = button(12)
testJoy = joystick([21,20])
testLives = lives([23,24])

moveMotor = motor([5,6,13,19])
punchMotor = motor([25,8,7,1])

testRobot = robot([25,8,7,1],[5,6,13,19],[23,24],12)
testuser = user([25,8,7,1],[5,6,13,19],[23,24],12,[21,20],16)

while testuser.get_lives() > 0:
    testuser.punch()
    testuser.move()
    testuser.is_hit()