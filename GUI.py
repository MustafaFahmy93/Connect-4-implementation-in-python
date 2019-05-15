#IMPORTS
import cv2 as cv
import numpy as np
import math
from backend_v5 import *
import time
import threading
thread = []
#GLOBAL VARIABLES
ix,iy = -1,-1
cenX,cenY = 0,0
turn = "us"
board = np.zeros((6,7))
img = np.zeros((710,720,3), np.uint8)
win=False
#FUNCTIONS
def createBoard():
    global img
    imgageCreated = np.zeros((710,720,3), np.uint8)
    h = imgageCreated.shape[0]
    w = imgageCreated.shape[1]
    for y in range(0, h):
        for x in range(0, w):
            imgageCreated[y, x]=(255,0,0)
    for i in range (6):
        y=140+(i*100)
        for j in range (7):
            x=60+(j*100)
            cv.circle(imgageCreated,(x,y), 40, (255,255,255), -1)
    return imgageCreated
        
def getCenters(img): #I DIDN'T USE IT ANYWAYS
    centersX = np.zeros((6,7),np.uint16)
    centersY = np.zeros((6,7),np.uint16)      
    for i in range (6):
        y=140+(i*100)
        for j in range (7):
            x=60+(j*100)
            centersX[i,j]=x
            centersY[i,j]=y

def calculateColumn(x):
    col=math.ceil((ix)/100)
    return col
end=False      
def guiEvents(event,x,y,flags,param): 
    global turn
    global ix,iy
    global board
    global cenX, cenY
    global img,win
    global end
    if event == cv.EVENT_LBUTTONDOWN and end == False:
        ix,iy = x,y
        if(turn == "us"): #Play and switch turn
            col = calculateColumn(x)
            if(board[5,col-1]== 1 or board[5,col-1]== 2): #COLUMN IS FULL, FORBIDDEN MOVE
                return
            center(col)
            if(check_winner(board,1)):
                print("player 1 is winner")
                end=True
                win=True
            turn = "them"
            cv.circle(img,(cenX,cenY), 40, (0,0,255), -1)
def ai_turn():
    global turn,img
    global board,win,end
    global cenX, cenY
    while(True):
        if(turn == "them" and end == False):
                col=minimax(5, board, True, -math.inf, math.inf)[0]
                col=col+1
                print(board)
                if(board[4,col-1]== 1 or board[5,col-1]== 2): #COLUMN IS FULL, FORBIDDEN MOVE
                    return
                center(col)
                if(check_winner(board,2)):
                    print("player 2 is winner")
                    end=True
                    win=True
                turn= "us"
                cv.circle(img,(cenX,cenY), 40, (0,255,0), -1)
def center(col): #GET CENTER OF NEXT PLACE TO PLAY IN
    global turn
    global board
    global img
    global cenX, cenY
    for i in range(6):
        if(board[i,col-1]==0 and turn == "us"):
            board[i,col-1]=1
            cenY=140+((5-i)*100)
            cenX=60+((col-1)*100)
            break
        elif(board[i,col-1]==0 and turn == "them"):
            board[i,col-1]=2
            cenY=140+((5-i)*100)
            cenX=60+((col-1)*100)
            break
    
#MAIN FUNCTION
def main():
    global img,win,turn
    img = createBoard()
    cv.namedWindow('image')
    cv.setMouseCallback('image',guiEvents)
    while(1):
        cv.imshow("image",img)
        k = cv.waitKey(20) & 0xFF
        if k == 27:
            break
        elif k == 97:
            turn="them"

    cv.destroyAllWindows()
t2 = threading.Thread(target=main, args=[])
t2.start()
t1 = threading.Thread(target=ai_turn, args=[])
t1.start()
