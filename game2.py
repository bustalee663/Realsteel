from threading import Thread
import time
from user import user
import RPi.GPIO as GPIO

player1 = user([25,8,7,1],[5,6,13,19],[23,24],12,[21,20],16)
player2 = user([2,3,4,9],[10,11,14,15],[17,18],22,[26,27],28)

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
    t2 = Thread(target=game, args=(player2))
    t2.start()
    game(player1)
    
if __name__=="__main__":
    main()