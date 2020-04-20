from time import sleep
from user import user
from robot import robot
from led import LED
from lives import lives
from joystick import joystick
from motor import motor
from button import button

# 4 punch motor pins, 4 move pins, 2 life pins, 1 hit pin, 2 joy pins, 1 punch pin

player1 = user([6,13,19,26],[12,16,20,21],[3,2],7,[15,18],24)
player2 = user([11,0,5,1],[27,22,10,9],[17,4],23,[8,25],14)

while True:
    print("Player 1 punch")
    player1.robot.punchMotor.move_left_deg(50)
    '''
    sleep(1)
    print("Player 2 punch")
    player2.robot.punchMotor.move_right_deg(90)
    sleep(1)
    print("Player 1 move")
    player1.robot.moveMotor.move_left_deg(90)
    sleep(1)
    print("Player 2 move")
    player2.robot.moveMotor.move_left_deg(90)
    '''
    break