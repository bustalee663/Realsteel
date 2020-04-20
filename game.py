from threading import Thread
import time
from user import user
import RPi.GPIO as GPIO

from threading import Thread
import time
from user import user
import RPi.GPIO as GPIO

# 4 punch motor pins, 4 move pins, 2 life pins, 1 hit pin, 2 joy pins, 1 punch pin

def game(player1, player2):
    while True:
        while True:
            player1.user_input()
            if player1.get_lives() == 0:
                break
        player1.victory = True
        player2.victory = True
        
        # Flash the victory lights and rub it in that hoe's face
        if player1.get_lives() == 0:
            for _ in range(4):
                player2.robot.lives.led1.on()
                player2.robot.lives.led2.on()
                time.sleep(0.25)
                player2.robot.lives.led1.off()
                player2.robot.lives.led2.off()
                time.sleep(0.25)
        time.sleep(2)
        
        player1.robot.lives.reset()
        player2.robot.lives.reset()
        player1.victory = False
        player2.victory = False
        
def main():
    player1 = user([6,13,19,26],[12,16,20,21],[3,2],7,[15,18],24)
    player2 = user([11,0,5,1],[27,22,10,9],[17,4],23,[8,25],14)
    t2 = Thread(target=game, args=(player2, player1))
    t2.start()
    game(player1, player2)
    
if __name__=="__main__":
    main()


def game(player):
    global player1
    global player2
    while True:
        while True:
            player.user_input()
            if player.get_lives() == 0:
                break
        player1.victory = True
        player2.victory = True
        time.sleep(5)
        player1.robot.lives.reset()
        player2.robot.lives.reset()
        player1.victory = False
        player2.victory = False
        
def main():
    #t2 = Thread(target=game, args=(player1,))
    #t2.start()
    game(player2)
    
if __name__=="__main__":
    main()