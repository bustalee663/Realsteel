from threading import Thread
import time
from user import user
import RPi.GPIO as GPIO

player1 = user([25,8,7,1],[5,6,13,19],[23,24],12,[21,20],16)
player2 = user([2,3,4,9],[10,11,14,15],[17,18],22,[26,27],28)

def setupThreads():
    t1 = Thread(target=player1.user_input, args=())
    t2 = Thread(target=player2.user_input, args=())
    
    t1.start()
    t2.start()
    
def resetGame():
    global player1
    global player2
    player1.robot.lives.reset()
    player2.robot.lives.reset()
    player1.victory = False
    player2.victory = False
    setupThreads()
    
def player1_victory():
    player1.victory = True
    player2.victory = True
    player1.robot.lives.reset()
    
def player2_victory():
    player1.victory = True
    player2.victory = True
    player2.robot.lives.reset()
    
def main():
    global player1
    global player2
    resetGame()
    while True:
        while True:
            if player1.get_lives() == 0:
                player2_victory()
                break  
            if player2.get_lives() == 0:
                player1_victory()
                break
        time.sleep(5)
        resetGame()
    
if __name__=="__main__":
    main()
    
    