#!/usr/bin/env python
# coding: utf-8




import cv2 as cv
import numpy as np
import math



ix,iy = -1,-1
cenX,cenY = 0,0
board = np.zeros((6,7),np.uint8)
def getXY(event,x,y,flags,param):
    global ix,iy
    global board
    global cenX, cenY
    global img
    if event == cv.EVENT_LBUTTONDOWN:
        ix,iy = x,y
        print(ix,iy)
        col = calculateCol(x)
        fill(col)
        cv.circle(img,(cenX,cenY), 40, (0,0,255), -1)
        print(board)
        
def fill(col):
    global board
    global img
    global cenX, cenY
    for i in range(6):
        if(board[5-i,col-1]==0):
            board[5-i,col-1]=1
            cenY=140+((5-i)*100)
            cenX=60+((col-1)*100)
            break

def calculateCol(x):
    col=math.ceil((ix)/100)
    return col





img = np.zeros((710,720,3), np.uint8)
h = img.shape[0]
w = img.shape[1]
for y in range(0, h):
    for x in range(0, w):
        img[y, x]=(255,0,0)

centersX = np.zeros((6,7),np.uint16)
centersY = np.zeros((6,7),np.uint16)
        
for i in range (6):
    y=140+(i*100)
    for j in range (7):
        x=60+(j*100)
        cv.circle(img,(x,y), 40, (255,255,255), -1)
        centersX[i,j]=x
        centersY[i,j]=y

cv.namedWindow('image')
cv.setMouseCallback('image',getXY)

while(1):
    cv.imshow("image",img)
    cv.waitKey()
cv.destroyAllWindows()

