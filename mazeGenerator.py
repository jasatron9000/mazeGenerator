import numpy as np
from random import seed, randint, random
import datetime as time

def generateNewMaze(height, width):
    emptyMaze = np.zeros([(height * 2) + 1, (width * 2) + 1])

    # fill up the nodes
    for i in range(height * 2):
        for j in range(width * 2):
            if i % 2 == 1 and j % 2 == 1:
                emptyMaze[i][j] = 1

    return emptyMaze

def backstepping(emptyMaze):
    #Get the height and width of the maze
    height = int((emptyMaze.shape[0] - 1) / 2)
    width = int((emptyMaze.shape[1] - 1) / 2)

    print(height, width)

    newMaze = emptyMaze
    backTracker = np.zeros([height, width])
    listOfPrevPosition = []

    #Pick random point
    x = time.datetime.now()
    seed(x.year + x.day * x.month * x.hour + x.minute * x.second)
    currentPos = [randint(0,height-1), randint(0,width-1)]
    backTracker[currentPos[0], currentPos[1]] = 1
    listOfPrevPosition.append(currentPos)

    while True:
        possibleMoves = getNewPos(backTracker, currentPos, 0)
        # print("\OLD POSITION: ")
        # print(currentPos)

        if (len(possibleMoves) != 0):
            #Edit the backTracker map and record previous location
            newPos = possibleMoves[randint(0,len(possibleMoves) - 1)]
            backTracker[newPos[0], newPos[1]] = 1
            listOfPrevPosition.append(newPos)
            
            #Edit the actual map
            moveH = int((((newPos[0] * 2) + 1) - ((currentPos[0] * 2) + 1)) / 2)
            moveW = int((((newPos[1] * 2) + 1) - ((currentPos[1] * 2) + 1)) / 2)    
            newMaze[((currentPos[0] * 2) + 1) + moveH][((currentPos[1] * 2) + 1) + moveW] = 1

            #Edit current position
            currentPos = newPos
            
        #If there is no free space
        else:
            # print("NO FREE SPACE")
            # print(currentPos)
            if listOfPrevPosition[0] == currentPos:
                return newMaze
            
            else:
                currentPos = listOfPrevPosition[len(listOfPrevPosition) - 2]
                backTracker[listOfPrevPosition[len(listOfPrevPosition) - 1][0], listOfPrevPosition[len(listOfPrevPosition) - 1][1]] = 2
                listOfPrevPosition.pop(len(listOfPrevPosition) - 1)
        
        # print("\nCURRENT POSITION: ")
        # print(currentPos)
        
        # print("\nPOSSIBLE MOVES: ")
        # print(possibleMoves)

        # print("\nPREV POSITIONS:")
        # print(listOfPrevPosition)

        # print(newMaze)
        # print("==========================================")
        # print(backTracker)
        # print("==========================================")
        # test = input("PRESS ENTER TO CONTINUE")
        # print("==========================================")

def finalPass(map, percentage):
    currentMap = map
    
    for i in range(2, currentMap.shape[0] - 2):
        for j in range(2, currentMap.shape[1] - 2):
            if currentMap[i][j] == 0:
                possibleMoves = getNewPos(currentMap, [i, j], 1)
                randomChoice = random() * 1000 <= percentage*1000

                if len(possibleMoves) == 2 and ((possibleMoves[0][0] == possibleMoves[1][0]) or (possibleMoves[0][1] == possibleMoves[1][1])):
                    #print(randomChoice)
                    
                    if randomChoice:
                        currentMap[i][j] = 1
    
    return currentMap

#HELPER FUNCTIO
def getNewPos(map, position, target):
    possibleLoc = []
    #Check up
    if (position[0] - 1) >= 0:
        currentTarget = map[position[0] - 1][position[1]]

        if currentTarget == target:
            possibleLoc.append([position[0] - 1, position[1]])
    
    #Check down
    if (position[0] + 1) < map.shape[0]:
        currentTarget = map[position[0] + 1][position[1]]

        if currentTarget == target:
            possibleLoc.append([position[0] + 1, position[1]])
    
    #Check left
    if (position[1] - 1) >= 0:
        currentTarget = map[position[0]][position[1] - 1]

        if currentTarget == target:
            possibleLoc.append([position[0], position[1] - 1])
    
    #Check right
    if (position[1] + 1) < map.shape[1]:
        currentTarget = map[position[0]][position[1] + 1]

        if currentTarget == target:
            possibleLoc.append([position[0], position[1] + 1])
    
    return possibleLoc