from user import user
from robot import robot
from led import LED
from lives import lives
from joystick import joystick
from motor import motor
from button import button

# 4 punch motor pins, 4 move pins, 2 life pins, 1 hit pin, 2 hit pins, 1 punch pin
testMotor = motor([5,6,13,19])

while True:
    testMotor.move_right()