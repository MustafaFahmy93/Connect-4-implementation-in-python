import numpy as np
from math import inf
import random
board = np.zeros((6,7),np.uint8)
from scoring import *
ai=2
player=1
def check_winner(board,player):
    board_tmp=board.copy()
    for y in range(6):#right to left
        for x in range(7):
            if((x+3<7) and board_tmp[y,x]==player and board_tmp[y,x+1]==player and board_tmp[y,x+2]==player and board_tmp[y,x+3]==player ):
                return True
    for x in range(7):#up to down
        for y in range(6):
            if((y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x]==player and board_tmp[y+2,x]==player and board_tmp[y+3,x]==player):
                return True
    for y in range(6):#diagonal  /
        for x in range(7):
            if((x+3<7) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==player):
                return True
    for y in range(3,6):#diagonal  \
        for x in range(3):
            if((x-3>0) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x-1]==player and board_tmp[y+2,x-2]==player and board_tmp[y+3,x-3]==player):
                return True
    return False
def children_count(board):
    child=0
    
    for col in range(7):
        for row in (range(6)):
            if(board[row,col]==0):
                child+=1
                break
    return child
def move_list(board):
    mlist=[]
    board_tmp=board.copy()
    n_child=children_count(board_tmp)
    for col in range(7):
         for row in (range(6)):
            if(board_tmp[row,col]==0 and n_child>0):
                n_child-=1
                mlist.append(str(row)+str(col))
                break
    return mlist
# Returns optimal value for current player  
#(Initially called for root and maximizer)  
def minimax(depth, board, maximizingPlayer, alpha, beta):
	#print(board)
	if depth == 0:
		return (None, score(board))
	if maximizingPlayer:
		value = -inf
		for m in move_list(board):
			b_copy = board.copy()
			b_copy[int(m[0]),int(m[1])]=ai
			new_score = minimax(depth-1,b_copy,False, alpha, beta)[1]
			if new_score > value:
				value = new_score
				column = int(m[1])
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else: # Minimizing player
		value = inf
		for m in move_list(board):
			b_copy = board.copy()
			b_copy[int(m[0]),int(m[1])]=player
			new_score = minimax(depth-1,b_copy,True, alpha, beta)[1]
			if new_score < value:
				value = new_score
				column = int(m[1])
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value
