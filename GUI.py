#IMPORTS
import cv2 as cv
import numpy as np
import math
import random

#GLOBAL VARIABLES
ix,iy = -1,-1
cenX,cenY = 0,0
turn = "us"
board = np.zeros((6,7),np.uint8)
img = np.zeros((710,720,3), np.uint8)

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
        
def guiEvents(event,x,y,flags,param): 
    global turn
    global ix,iy
    global board
    global cenX, cenY
    global img
    if event == cv.EVENT_LBUTTONDOWN:
        ix,iy = x,y
        if(turn == "us"): #Play and switch turn
            col = calculateColumn(x)
            if(board[0,col-1]== 1 or board[0,col-1]== 2): #COLUMN IS FULL, FORBIDDEN MOVE
                return
            center(col)
            turn = "them"
            cv.circle(img,(cenX,cenY), 40, (0,0,255), -1)
        elif(turn == "them"):
            col = random.randint(1,6)
            if(board[0,col-1]== 1 or board[0,col-1]== 2): #COLUMN IS FULL, FORBIDDEN MOVE
                return
            center(col)
            turn= "us"
            cv.circle(img,(cenX,cenY), 40, (0,255,0), -1)
        
def center(col): #GET CENTER OF NEXT PLACE TO PLAY IN
    global turn
    global board
    global img
    global cenX, cenY
    for i in range(6):
        if(board[5-i,col-1]==0 and turn == "us"):
            board[5-i,col-1]=1
            cenY=140+((5-i)*100)
            cenX=60+((col-1)*100)
            break
        elif(board[5-i,col-1]==0 and turn == "them"):
            board[5-i,col-1]=2
            cenY=140+((5-i)*100)
            cenX=60+((col-1)*100)
            break

#MAIN FUNCTION
def main():
    global img
    img = createBoard()
    cv.namedWindow('image')
    cv.setMouseCallback('image',guiEvents)
    while(1):
        cv.imshow("image",img)
        k = cv.waitKey(20) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()
    
    
if __name__ =='__main__':
    main()
