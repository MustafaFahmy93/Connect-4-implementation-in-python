import numpy as np
board = np.zeros((6,7),np.uint8)
print(board)
us=1
them=2
##for x in range(7):
##    for y in range(6):
##        if(y==5 and x%2==0):
##            board[y,x]=1
##        if(y==5 and x%2==1):
##            board[y,x]=2

def fill_empty_cells(board,player):
    board_tmp=board.copy()
    for x in range(7):
        for y in range(6):
            if(board[y,x]==0):
                board_tmp[y,x]=player
    return board_tmp
def num_of_wins(board_tmp,player):
    board_tmp=fill_empty_cells(board_tmp,player)
    count=0
    for y in range(6):#right to left
        for x in range(7):
            if((x+3<7) and board_tmp[y,x]==player and board_tmp[y,x+1]==player and board_tmp[y,x+2]==player and board_tmp[y,x+3]==player ):
                count+=1
    for x in range(7):#up to down
        for y in range(6):
            if((y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x]==player and board_tmp[y+2,x]==player and board_tmp[y+3,x]==player):
                count+=1
    for y in range(6):#diagonal
        for x in range(7):
            if((x+3<7) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==player):
                count+=1
    return count
def check_winner(board,player):
    board_tmp=fill_empty_cells(board,player)
    for y in range(6):#right to left
        for x in range(7):
            if((x+3<7) and board_tmp[y,x]==player and board_tmp[y,x+1]==player and board_tmp[y,x+2]==player and board_tmp[y,x+3]==player ):
                return True
    for x in range(7):#up to down
        for y in range(6):
            if((y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x]==player and board_tmp[y+2,x]==player and board_tmp[y+3,x]==player):
                return True
    for y in range(6):#diagonal
        for x in range(7):
            if((x+3<7) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==player):
                return True
    return False


def children_count(board):
    child=0
    for x in range(7):
        for y in reversed(range(6)):
            if(board[y,x]==0):
                child+=1
                break
    return child


level=0
def alph_beta(initial_board,depth,player):
    global level,us,them
    alph=-1000
    beta=1000
    board_tmp=initial_board.copy()
    if(depth==level):
        
        return 
    for c in range(children_count(board_tmp)):
        for y in reversed(range(6)):
            for x in range(7):
                if(board_tmp[y,x]==0 and flag==0):
                    board_tmp[y,x]=player
                    if(check_winner(board_tmp,player)):
                        return 
                    if(player==us):
                        player=them
                    else:
                        player=us
                    level+=1
                    alph_beta(board_tmp,level,player)
                
    return [alph,beta] 

##build_tree(board,3,us)
##print(tree)
    
       
print("x")
print(children_count(board))           
print("x")
def main():
    utility_fun=num_of_wins(board,us)-num_of_wins(board,them)
    print(utility_fun)
##    print(build_tree(board,1))
##    print(build_tree(board,1))
if __name__ == '__main__':
    main()