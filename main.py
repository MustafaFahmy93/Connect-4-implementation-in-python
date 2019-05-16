# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv
import numpy as np
import math
from backend_v5 import *
import time
import threading
thread = []
depth=2
select1_flag=0
select2_flag=0
class Ui_ConnectFour(object):
	def setupUi(self, ConnectFour):
		ConnectFour.setObjectName("ConnectFour")
		ConnectFour.resize(739, 500)
		self.centralwidget = QtWidgets.QWidget(ConnectFour)
		self.centralwidget.setObjectName("centralwidget")
		self.btn = QtWidgets.QPushButton(self.centralwidget)
		self.btn.setGeometry(QtCore.QRect(290, 380, 122, 34))
		self.btn.setObjectName("btn")
		self.btn.clicked.connect(myfn)
		self.l2 = QtWidgets.QLabel(self.centralwidget)
		self.l2.setGeometry(QtCore.QRect(400, 150, 191, 22))
		self.l2.setObjectName("l2")
		self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
		self.rb3.setGeometry(QtCore.QRect(550, 100, 139, 27))
		self.rb3.setObjectName("radioButton")
		self.rb4= QtWidgets.QRadioButton(self.centralwidget)
		self.rb4.setGeometry(QtCore.QRect(550, 150, 139, 27))
		self.rb4.setObjectName("radioButton_2")
		self.rb5= QtWidgets.QRadioButton(self.centralwidget)
		self.rb5.setGeometry(QtCore.QRect(550, 200, 139, 27))
		self.rb5.setObjectName("radioButton_3")
		#self.rb3.setChecked(1)
		self.rb3.toggled.connect(lambda:self.btnstate1(self.rb3))
		self.rb4.toggled.connect(lambda:self.btnstate1(self.rb4))
		self.rb5.toggled.connect(lambda:self.btnstate1(self.rb5))
		self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox.setGeometry(QtCore.QRect(50, 40, 200, 250))
		self.groupBox.setTitle("")
		self.groupBox.setObjectName("groupBox")
		self.groupBox.setFlat(1)
		self.groupBox.setStyleSheet("border:0;")
		self.rb2 = QtWidgets.QRadioButton(self.groupBox)
		self.rb2.setGeometry(QtCore.QRect(0, 130, 201, 27))
		self.rb2.setObjectName("rb2")
		self.rb1 = QtWidgets.QRadioButton(self.groupBox)
		self.rb1.setGeometry(QtCore.QRect(0, 70, 139, 27))
		self.rb1.setObjectName("rb1")
		#self.rb1.setChecked(1)
		self.rb1.toggled.connect(lambda:self.btnstate(self.rb1))
		self.rb2.toggled.connect(lambda:self.btnstate(self.rb2))
		ConnectFour.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(ConnectFour)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 28))
		self.menubar.setObjectName("menubar")
		ConnectFour.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(ConnectFour)
		self.statusbar.setObjectName("statusbar")
		ConnectFour.setStatusBar(self.statusbar)
		self.retranslateUi(ConnectFour)
		QtCore.QMetaObject.connectSlotsByName(ConnectFour)

	def retranslateUi(self, ConnectFour):
		_translate = QtCore.QCoreApplication.translate
		ConnectFour.setWindowTitle(_translate("ConnectFour", "Connect_4"))
		self.btn.setText(_translate("ConnectFour", "Start"))
		self.l2.setText(_translate("ConnectFour", "Select Diffuclty:"))
		self.rb3.setText(_translate("ConnectFour", "Easy"))
		self.rb4.setText(_translate("ConnectFour", "Intermediate"))
		self.rb5.setText(_translate("ConnectFour", "Hard"))
		self.rb2.setText(_translate("ConnectFour", "Computer Starts"))
		self.rb1.setText(_translate("ConnectFour", "Player Starts"))
		


	def btnstate(self,b):
            global turn_flag,select1_flag
            if b.text() == "Player Starts":
                if b.isChecked() == True:
                    turn_flag='none'
                    select1_flag+=2
                    ##print (b.text()+" is selected")				
            if b.text() == "Computer Starts":
                if b.isChecked() == True:
                    turn_flag = 'them'
                    select1_flag+=2
                    ##print (b.text()+" is selected")

	def btnstate1(self,b):
            global depth,select2_flag
            if b.text() == "Easy":
                if b.isChecked() == True:
                    depth= 1
                    select2_flag+=1
                    #print (b.text()+" is selected")				
            if b.text() == "Intermediate":
                if b.isChecked() == True:
                    depth = 4
                    select2_flag+=1
                    #print (b.text()+" is selected")
            if b.text() == "Hard":
                if b.isChecked() == True:
                    depth = 6
                    select2_flag+=1
                    #print (b.text()+" is selected")
	
def myfn():
	#newfn1()
    global select1_flag,select2_flag
    if(select1_flag>0 and select2_flag>0):
        main()
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
            imgageCreated[y, x]=(235,235,235)
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
            if(isFull(board)):
                    cv.putText(img,"Draw", (170,80), cv.FONT_HERSHEY_COMPLEX, 3, (51,99,21),3)
                    end=True
            if(board[5,col-1]== 1 or board[5,col-1]== 2): #COLUMN IS FULL, FORBIDDEN MOVE
                return
            center(col)
            if(check_winner(board,1)):
                cv.putText(img,"You win", (150,80), cv.FONT_HERSHEY_COMPLEX, 3, (41,21,99),3)
                end=True
                win=True
            cv.circle(img,(cenX,cenY), 40, (0,0,255), -1)
            turn = "them"
def ai_turn():
    global turn,img
    global board,win,end
    global cenX, cenY,depth
    while(True):
        time.sleep(0.5)
        if(turn == "them" and end == False):
                col=minimax(depth, board, True, -math.inf, math.inf)[0]
                col=col+1
                ##print(board)
                if(isFull(board)):
                    cv.putText(img,"Draw", (170,80), cv.FONT_HERSHEY_COMPLEX, 3, (51,99,21),3)
                    end=True
                if(board[5,col-1]== 1 or board[5,col-1]== 2): #COLUMN IS FULL, FORBIDDEN MOVE
                    return
                center(col)
                if(check_winner(board,2)):
                    cv.putText(img,"Game Over", (90,80), cv.FONT_HERSHEY_COMPLEX, 3, (51,99,21),3)
                    end=True
                    win=True
                cv.circle(img,(cenX,cenY), 40, (0,255,0), -1)
                turn= "us"
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
    global img,win,turn,turn_flag
    img = createBoard()
    cv.namedWindow('Connect4')
    cv.setMouseCallback('Connect4',guiEvents)
    while(1):
        cv.imshow("Connect4",img)
        if(turn_flag=='them'):
            turn='them'
            turn_flag='none'
        k = cv.waitKey(20) & 0xFF
        if k == 27:
            break
        elif k == 97:
            turn="them"

    cv.destroyAllWindows()


# def newfn1():
# 	t2 = threading.Thread(target=main, args=[])
# 	t2.start()
t1 = threading.Thread(target=ai_turn, args=[])
t1.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConnectFour = QtWidgets.QMainWindow()
    ui = Ui_ConnectFour()
    ui.setupUi(ConnectFour)
    ConnectFour.show()
    sys.exit(app.exec_())
