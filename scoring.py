winner = []
gameScore = 100000
def score_position(board,row, column, delta_y, delta_x):
    global winner,gameScore
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
        winner= winningPlayer
        return -gameScore
    elif(aiScore == 4):
        winner = winningAI
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
            horizontalScores += gameScore

    for y in range (3):
        for x in range (4):
            score = score_position(board,y, x, 1, 1)
            if(score== gameScore):
                return gameScore
            if(score == -gameScore):
                return -gameScore
            diagonalScoresI += score

    for y in range(3,6):
        for x in range (3):
            score = score_position(board,y, x, -1, 1) 
            if(score == gameScore):
                return gameScore
            if(score == -gameScore):
                return -gameScore
            diagonalScoresII += score

    scores = horizontalScores + verticalScores + diagonalScoresI + diagonalScoresII
    return scores

