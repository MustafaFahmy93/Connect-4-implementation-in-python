import numpy as np
board = np.zeros((7,6),np.uint8)
us=1
them=2
for x in range(6):
    for y in range(7):
        if(y==6 and x%2==0):
            board[y,x]=1
        if(y==6 and x%2==1):
            board[y,x]=2

def fill_empty_cells(board,player):
    board_tmp=board.copy()
    for x in range(6):
        for y in range(7):
            if(board[y,x]==0):
                board_tmp[y,x]=player
    return board_tmp
def num_of_wins(board_tmp,player):
    board_tmp=fill_empty_cells(board_tmp,player)
    count=0
    for y in range(7):#right to left
        for x in range(6):
            if((x+3<6) and board_tmp[y,x]==player and board_tmp[y,x+1]==player and board_tmp[y,x+2]==player and board_tmp[y,x+3]==player ):
                count+=1
    for x in range(6):#up to down
        for y in range(7):
            if((y+3<7) and board_tmp[y,x]==player and board_tmp[y+1,x]==player and board_tmp[y+2,x]==player and board_tmp[y+3,x]==player):
                count+=1
    for y in range(7):#diagonal
        for x in range(6):
            if((x+3<6) and (y+3<7) and board_tmp[y,x]==player and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==player):
                count+=1
    return count
def check_winner(board,player):
    board_tmp=fill_empty_cells(board,player)
    for y in range(7):#right to left
        for x in range(6):
            if((x+3<6) and board_tmp[y,x]==player and board_tmp[y,x+1]==player and board_tmp[y,x+2]==player and board_tmp[y,x+3]==player ):
                return True
    for x in range(6):#up to down
        for y in range(7):
            if((y+3<7) and board_tmp[y,x]==player and board_tmp[y+1,x]==player and board_tmp[y+2,x]==player and board_tmp[y+3,x]==player):
                return True
    for y in range(7):#diagonal
        for x in range(6):
            if((x+3<6) and (y+3<7) and board_tmp[y,x]==player and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==player):
                return True
    return False
utility_fun=num_of_wins(board,us)-num_of_wins(board,them)
print(utility_fun)