# Python - Maze Generator
This is a simple maze generator in python used for a university project. This maze generator uses the **Recursive Backtracking** algorithm. 

The algorithm works like this:
1. Pick a starting cell in a generated map
2. Pick a cell that is adjacent to the current cell that the program is in that has not been vistited yet
3. If the all adjacent cells has been visited, move to the last cell that the program visited. Reapeat this step until there there is a free space.
4. Repeat steps 2 and 3 until the program back-tracked all the way to the starting point

More information here: http://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking

## Usage
Clone the folder and enter the command prompt inside the folder.
Type this command: ``python maze.py``
After this is done, a file called final.csv is generated.
