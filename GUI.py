#!/usr/bin/env python
# coding: utf-8


import cv2 as cv
import numpy as np
import math




ix,iy = -1,-1
board = np.zeros((6,7),np.uint8)
def getXY(event,x,y,flags,param):
    global ix,iy
    global board
    if event == cv.EVENT_LBUTTONDOWN:
        ix,iy = x,y
        print(ix,iy)
        col = calculateCol(x)
        fill(col)
        print(board)
        
def fill(col):
    global board
    for i in range(6):
        if(board[5-i,col-1]==0):
            board[5-i,col-1]=1
            break

def calculateCol(x):
    col=math.ceil((ix)/100)
    return col




img = np.zeros((710,720,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',getXY)
h = img.shape[0]
w = img.shape[1]
for y in range(0, h):
    for x in range(0, w):
        img[y, x]=(255,0,0)
for i in range (6):
    y=140+(i*100)
    for j in range (7):
        x=60+(j*100)
        cv.circle(img,(x,y), 40, (255,255,255), -1)

cv.imshow("image",img)
cv.waitKey()
cv.destroyAllWindows()

