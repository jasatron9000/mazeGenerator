import numpy as np
import mazeGenerator as mg
from random import seed, randint
import datetime as time
from matplotlib import pyplot as plt

#Maze Settings
height = 30
width = 25
percentage = 0.3

#Generate Maze with nodes
emptyMaze = mg.generateNewMaze(height, width)

#Apply the backstepping algorithm
firstPassMaze = mg.backstepping(emptyMaze)

#Apply the connection algorithm
finalMaze = mg.finalPass(firstPassMaze, percentage)
intMaze = finalMaze.astype(int)

#Reveal The Map
for i in range(finalMaze.shape[0]):
    for j in range(finalMaze.shape[1]):
        if finalMaze[i][j] == 0:
            print("[]", end = '')
        else:
            print("  ", end = '')
    print("")

#Save as cvs and image
np.savetxt('final.csv', intMaze, delimiter=',', fmt="%d")
plt.imshow(intMaze)
plt.show()