# winner = []
gameScore = 100000
def score_position(board,row, column, delta_y, delta_x):
    # global winner
    global gameScore
    aiScore=0
    playerScore=0
    winningAI=[]
    winningPlayer=[]

    for i in range (4):
        if (board[row,column]== 1):
            winningPlayer.append([row,column])
            playerScore+=1
        elif(board[row,column]== 2):
            winningAI.append([row,column])
            aiScore +=1

        row += delta_y
        column += delta_x

    if(playerScore == 4):
        # winner= winningPlayer
        return -gameScore
    elif(aiScore == 4):
        # winner = winningAI
        return gameScore
    else:
        return aiScore


def score(board):
    
    scores =0
    verticalScores=0
    horizontalScores=0
    diagonalScoresI=0
    diagonalScoresII=0

    for y in range (3):
        for x in range (7):
            score = score_position(board,y, x, 1, 0)
            if(score == gameScore):
                return gameScore
            if(score == -gameScore):
                return -gameScore
            verticalScores += gameScore
    
    for y in range (6):
        for x in range (4):
            score = score_position(board,y, x, 0, 1)
            if(score == gameScore):
                return gameScore
            if(score == -gameScore):
                return -gameScore
            horizontalScores += gameScore#+100000

    for y in range (3):
        for x in range (4):
            score = score_position(board,y, x, 1, 1)
            if(score== gameScore):
                return gameScore
            if(score == -gameScore):
                return -gameScore
            diagonalScoresI += score#+1

    for y in range(3,6):
        for x in range (4):
            score = score_position(board,y, x, -1, 1) 
            if(score == gameScore):
                return gameScore
            if(score == -gameScore):
                return -gameScore
            diagonalScoresII += score#+1

    scores = horizontalScores + verticalScores + diagonalScoresI + diagonalScoresII
    return scores

def scoreV2(board_tmp):
    ai=2
    player=1
    aiCount=0
    #==============0===============
    for y in range(6):#right to left
        for x in range(7):
            if((x+3<7)and board_tmp[y,x]==0 and board_tmp[y,x+1]==0 and board_tmp[y,x+2]==0 and board_tmp[y,x+3]==0):
                aiCount+=1
    for x in range(7):#up to down
        for y in range(6):
            if((y+3<6)and board_tmp[y,x]==0 and board_tmp[y+1,x]==0 and board_tmp[y+2,x]==0 and board_tmp[y+3,x]==0):
                aiCount+=1
    for y in range(6):#diagonal  \
        for x in range(7):
            if((x+3<7) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x+1]==0 and board_tmp[y+2,x+2]==0 and board_tmp[y+3,x+3]==0):
                aiCount+=1
    for y in range(6):#diagonal  /
        for x in range(7):
            if((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==0 and board_tmp[y+2,x-2]==0 and board_tmp[y+3,x-3]==0):
                aiCount+=1
    #==============1===============
    for y in range(6):#right to left
        for x in range(7):
            if((x+3<7)and board_tmp[y,x]==ai and board_tmp[y,x+1]==0 and board_tmp[y,x+2]==0 and board_tmp[y,x+3]==0):
                aiCount+=2
            elif((x+3<7)and board_tmp[y,x]==ai and board_tmp[y,x+1]==0 and board_tmp[y,x+2]==0 and board_tmp[y,x+3]==0):
                aiCount-=2
    for x in range(7):#up to down
        for y in range(6):
            if((y+3<6)and board_tmp[y,x]==ai and board_tmp[y+1,x]==0 and board_tmp[y+2,x]==0 and board_tmp[y+3,x]==0):
                aiCount+=2
            elif((y+3<6)and board_tmp[y,x]==ai and board_tmp[y+1,x]==0 and board_tmp[y+2,x]==0 and board_tmp[y+3,x]==0):
                aiCount-=2
    for y in range(6):#diagonal  \
        for x in range(7):
            if((x+3<7) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x+1]==0 and board_tmp[y+2,x+2]==0 and board_tmp[y+3,x+3]==0):
                aiCount+=2
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x+1]==0 and board_tmp[y+2,x+2]==0 and board_tmp[y+3,x+3]==0):
                aiCount-=2
    for y in range(6):#diagonal  /
        for x in range(7):
            if((x-3>=0) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x-1]==0 and board_tmp[y+2,x-2]==0 and board_tmp[y+3,x-3]==0):
                aiCount+=2
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x-1]==0 and board_tmp[y+2,x-2]==0 and board_tmp[y+3,x-3]==0):
                aiCount-=2
    #==============2===============
    for y in range(6):#right to left
        for x in range(7):
            if((x+3<7)and board_tmp[y,x]==ai and board_tmp[y,x+1]==ai and board_tmp[y,x+2]==0 and board_tmp[y,x+3]==0):#(0-ai-ai-0)
                aiCount+=3
            elif((x+3<7)and board_tmp[y,x]==0 and board_tmp[y,x+1]==ai and board_tmp[y,x+2]==ai and board_tmp[y,x+3]==0):#(0-0-ai-ai) and (ai-0-0-ai)
                aiCount+=3
            elif((x+3<7)and board_tmp[y,x]==ai and board_tmp[y,x+1]==0 and board_tmp[y,x+2]==0 and board_tmp[y,x+3]==ai):#(ai-0-0-ai)
                aiCount+=3
            elif((x+3<7)and board_tmp[y,x]==0 and board_tmp[y,x+1]==0 and board_tmp[y,x+2]==ai and board_tmp[y,x+3]==ai):#(0-0-ai-ai)
                aiCount+=3
            elif((x+3<7)and board_tmp[y,x]==player and board_tmp[y,x+1]==player and board_tmp[y,x+2]==0 and board_tmp[y,x+3]==0):#(0-player-player-0)
                aiCount-=5
            elif((x+3<7)and board_tmp[y,x]==0 and board_tmp[y,x+1]==player and board_tmp[y,x+2]==player and board_tmp[y,x+3]==0):#(0-0-player-player) and (ai-0-0-ai)
                aiCount-=5
            elif((x+3<7)and board_tmp[y,x]==player and board_tmp[y,x+1]==0 and board_tmp[y,x+2]==0 and board_tmp[y,x+3]==player):#(player-0-0-player)
                aiCount-=3
            elif((x+3<7)and board_tmp[y,x]==0 and board_tmp[y,x+1]==0 and board_tmp[y,x+2]==player and board_tmp[y,x+3]==player):#(0-0-player-player)
                aiCount-=5
    for x in range(7):#up to down
        for y in range(6):
            if((y+3<6)and board_tmp[y,x]==ai and board_tmp[y+1,x]==ai and board_tmp[y+2,x]==0 and board_tmp[y+3,x]==0):#(ai-ai-0-0)
                aiCount+=3
            elif((y+3<6)and board_tmp[y,x]==0 and board_tmp[y+1,x]==ai and board_tmp[y+2,x]==ai and board_tmp[y+3,x]==0):#(0-ai-ai-0)
                aiCount+=3
            elif((y+3<6)and board_tmp[y,x]==0 and board_tmp[y+1,x]==0 and board_tmp[y+2,x]==ai and board_tmp[y+3,x]==ai):#(0-0-ai-ai)
                aiCount+=3
            elif((y+3<6)and board_tmp[y,x]==ai and board_tmp[y+1,x]==0 and board_tmp[y+2,x]==0 and board_tmp[y+3,x]==ai):#(ai-0-0-ai)
                aiCount+=3
            elif((y+3<6)and board_tmp[y,x]==player and board_tmp[y+1,x]==player and board_tmp[y+2,x]==0 and board_tmp[y+3,x]==0):#(player-player-0-0)
                aiCount-=3
            elif((y+3<6)and board_tmp[y,x]==0 and board_tmp[y+1,x]==player and board_tmp[y+2,x]==player and board_tmp[y+3,x]==0):#(0-player-player-0)
                aiCount-=3
            elif((y+3<6)and board_tmp[y,x]==0 and board_tmp[y+1,x]==0 and board_tmp[y+2,x]==player and board_tmp[y+3,x]==player):#(0-0-player-player)
                aiCount-=3
            elif((y+3<6)and board_tmp[y,x]==player and board_tmp[y+1,x]==0 and board_tmp[y+2,x]==0 and board_tmp[y+3,x]==player):#(player-0-0-player)
                aiCount-=3
    for y in range(6):#diagonal  \
        for x in range(7):
            if((x+3<7) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x+1]==ai and board_tmp[y+2,x+2]==0 and board_tmp[y+3,x+3]==0):#(ai-ai-0-0)
                aiCount+=3
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x+1]==ai and board_tmp[y+2,x+2]==ai and board_tmp[y+3,x+3]==0):#(0-ai-ai-0)
                aiCount+=3
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x+1]==0 and board_tmp[y+2,x+2]==ai and board_tmp[y+3,x+3]==ai):#(0-0-ai-ai)
                aiCount+=3
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x+1]==0 and board_tmp[y+2,x+2]==0 and board_tmp[y+3,x+3]==ai):#(ai-0-0-ai)
                aiCount+=3
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==0 and board_tmp[y+3,x+3]==0):#(player-player-0-0)
                aiCount-=3
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==0):#(0-player-player-0)
                aiCount-=3
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x+1]==0 and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==player):#(0-0-player-player)
                aiCount-=3
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x+1]==0 and board_tmp[y+2,x+2]==0 and board_tmp[y+3,x+3]==player):#(player-0-0-player)
                aiCount-=3
    for y in range(6):#diagonal  /
        for x in range(7):
            if((x-3>=0) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x-1]==ai and board_tmp[y+2,x-2]==0 and board_tmp[y+3,x-3]==0):#(ai-ai-0-0)
                aiCount+=3
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==ai and board_tmp[y+2,x-2]==ai and board_tmp[y+3,x-3]==0):#(0-ai-ai-0)
                aiCount+=3
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==0 and board_tmp[y+2,x-2]==ai and board_tmp[y+3,x-3]==ai):#(0-0-ai-ai)
                aiCount+=3
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==ai and board_tmp[y+2,x-2]==ai and board_tmp[y+3,x-3]==0):#(0-ai-ai-0)
                aiCount+=3
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x-1]==player and board_tmp[y+2,x-2]==0 and board_tmp[y+3,x-3]==0):#(player-player-0-0)
                aiCount-=3
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==player and board_tmp[y+2,x-2]==player and board_tmp[y+3,x-3]==0):#(0-player-player-0)
                aiCount-=3
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==0 and board_tmp[y+2,x-2]==player and board_tmp[y+3,x-3]==player):#(0-0-player-player)
                aiCount-=3
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==player and board_tmp[y+2,x-2]==player and board_tmp[y+3,x-3]==0):#(0-player-player-0)
                aiCount-=3
    #==============3===============
    for y in range(6):#right to left
        for x in range(7):
            if((x+3<7)and board_tmp[y,x]==ai and board_tmp[y,x+1]==ai and board_tmp[y,x+2]==ai and board_tmp[y,x+3]==0):#(ai-ai-ai-0)
                aiCount+=5
            elif((x+3<7)and board_tmp[y,x]==0 and board_tmp[y,x+1]==ai and board_tmp[y,x+2]==ai and board_tmp[y,x+3]==ai):#(0-ai-ai-ai)
                aiCount+=5
            elif((x+3<7)and board_tmp[y,x]==ai and board_tmp[y,x+1]==0 and board_tmp[y,x+2]==ai and board_tmp[y,x+3]==ai):#(ai-0-ai-ai)
                aiCount+=5
            elif((x+3<7)and board_tmp[y,x]==0 and board_tmp[y,x+1]==ai and board_tmp[y,x+2]==ai and board_tmp[y,x+3]==ai):#(0-ai-ai-ai)
                aiCount+=5
            elif((x+3<7)and board_tmp[y,x]==player and board_tmp[y,x+1]==player and board_tmp[y,x+2]==player and board_tmp[y,x+3]==0):#(player-player-player-0)
                aiCount-=7
            elif((x+3<7)and board_tmp[y,x]==0 and board_tmp[y,x+1]==player and board_tmp[y,x+2]==player and board_tmp[y,x+3]==player):#(0-player-player-player)
                aiCount-=7
            elif((x+3<7)and board_tmp[y,x]==player and board_tmp[y,x+1]==0 and board_tmp[y,x+2]==player and board_tmp[y,x+3]==player):#(player-0-player-player)
                aiCount-=7
            elif((x+3<7)and board_tmp[y,x]==0 and board_tmp[y,x+1]==player and board_tmp[y,x+2]==player and board_tmp[y,x+3]==player):#(0-player-player-player)
                aiCount-=7
    for x in range(7):#up to down
        for y in range(6):
            if((y+3<6)and board_tmp[y,x]==ai and board_tmp[y+1,x]==ai and board_tmp[y+2,x]==ai and board_tmp[y+3,x]==0):#(ai-ai-ai-0)
                aiCount+=5
            elif((y+3<6)and board_tmp[y,x]==0 and board_tmp[y+1,x]==ai and board_tmp[y+2,x]==ai and board_tmp[y+3,x]==ai):#(0-ai-ai-ai)
                aiCount+=5
            elif((y+3<6)and board_tmp[y,x]==ai and board_tmp[y+1,x]==0 and board_tmp[y+2,x]==ai and board_tmp[y+3,x]==ai):#(ai-0-ai-ai)
                aiCount+=5
            elif((y+3<6)and board_tmp[y,x]==ai and board_tmp[y+1,x]==ai and board_tmp[y+2,x]==0 and board_tmp[y+3,x]==ai):#(ai-ai-0-ai)
                aiCount+=5
            elif((y+3<6)and board_tmp[y,x]==player and board_tmp[y+1,x]==player and board_tmp[y+2,x]==player and board_tmp[y+3,x]==0):#(player-player-player-0)
                aiCount-=5
            elif((y+3<6)and board_tmp[y,x]==0 and board_tmp[y+1,x]==player and board_tmp[y+2,x]==player and board_tmp[y+3,x]==player):#(0-player-player-player)
                aiCount-=5
            elif((y+3<6)and board_tmp[y,x]==player and board_tmp[y+1,x]==0 and board_tmp[y+2,x]==player and board_tmp[y+3,x]==player):#(player-0-player-player)
                aiCount-=5
            elif((y+3<6)and board_tmp[y,x]==player and board_tmp[y+1,x]==player and board_tmp[y+2,x]==0 and board_tmp[y+3,x]==player):#(player-player-0-player)
                aiCount-=5
    for y in range(6):#diagonal  \
        for x in range(7):
            if((x+3<7) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x+1]==ai and board_tmp[y+2,x+2]==ai and board_tmp[y+3,x+3]==0):#(ai-ai-ai-0)
                aiCount+=7
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x+1]==ai and board_tmp[y+2,x+2]==ai and board_tmp[y+3,x+3]==ai):#(0-ai-ai-ai)
                aiCount+=7
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x+1]==0 and board_tmp[y+2,x+2]==ai and board_tmp[y+3,x+3]==ai):#(ai-0-ai-ai)
                aiCount+=7
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x+1]==ai and board_tmp[y+2,x+2]==ai and board_tmp[y+3,x+3]==ai):#(0-ai-ai-ai)
                aiCount+=7
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==0):#(player-player-player-0)
                aiCount-=5
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==player):#(0-player-player-player)
                aiCount-=5
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x+1]==0 and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==player):#(player-0-player-player)
                aiCount-=5
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==player):#(0-player-player-player)
                aiCount-=5
    for y in range(6):#diagonal  /
        for x in range(7):
            if((x-3>=0) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x-1]==ai and board_tmp[y+2,x-2]==ai and board_tmp[y+3,x-3]==0):#(ai-ai-ai-0)
                aiCount+=7
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==ai and board_tmp[y+2,x-2]==ai and board_tmp[y+3,x-3]==ai):#(0-ai-ai-ai)
                aiCount+=7
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x-1]==0 and board_tmp[y+2,x-2]==ai and board_tmp[y+3,x-3]==ai):#(ai-0-ai-ai)
                aiCount+=7
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==ai and board_tmp[y+2,x-2]==ai and board_tmp[y+3,x-3]==ai):#(0-ai-ai-ai)
                aiCount+=7
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x-1]==player and board_tmp[y+2,x-2]==player and board_tmp[y+3,x-3]==0):#(player-player-player-0)
                aiCount-=5
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==player and board_tmp[y+2,x-2]==player and board_tmp[y+3,x-3]==player):#(0-player-player-player)
                aiCount-=5
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x-1]==0 and board_tmp[y+2,x-2]==player and board_tmp[y+3,x-3]==player):#(player-0-player-player)
                aiCount-=5
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==0 and board_tmp[y+1,x-1]==player and board_tmp[y+2,x-2]==player and board_tmp[y+3,x-3]==player):#(0-player-player-player)
                aiCount-=5
    #==============4===============
    for y in range(6):#right to left
        for x in range(7):
            if((x+3<7) and board_tmp[y,x]==ai and board_tmp[y,x+1]==ai and board_tmp[y,x+2]==ai and board_tmp[y,x+3]==ai ):
                aiCount+=100
            elif((x+3<7) and board_tmp[y,x]==player and board_tmp[y,x+1]==player and board_tmp[y,x+2]==player and board_tmp[y,x+3]==player ):
                aiCount-=50
    for x in range(7):#up to down
        for y in range(6):
            if((y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x]==ai and board_tmp[y+2,x]==ai and board_tmp[y+3,x]==ai):
                aiCount+=100
            elif((y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x]==player and board_tmp[y+2,x]==player and board_tmp[y+3,x]==player):
                aiCount-=50
    for y in range(6):#diagonal  \
        for x in range(7):
            if((x+3<7) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x+1]==ai and board_tmp[y+2,x+2]==ai and board_tmp[y+3,x+3]==ai):
                aiCount+=100
            elif((x+3<7) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x+1]==player and board_tmp[y+2,x+2]==player and board_tmp[y+3,x+3]==player):
                aiCount-=50
    for y in range(6):#diagonal  /
        for x in range(7):
            if((x-3>=0) and (y+3<6) and board_tmp[y,x]==ai and board_tmp[y+1,x-1]==ai and board_tmp[y+2,x-2]==ai and board_tmp[y+3,x-3]==ai):
                aiCount+=100
            elif((x-3>=0) and (y+3<6) and board_tmp[y,x]==player and board_tmp[y+1,x-1]==player and board_tmp[y+2,x-2]==player and board_tmp[y+3,x-3]==player):
                aiCount-=50
    return aiCount
