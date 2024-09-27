#sudoku solver
"""Solves basic sudoku puzzles using backtracking algorithm"""

#set up board - 0 is empty digit
board = [
[7,8,0,4,0,0,1,2,0],
[6,0,0,0,7,5,0,0,9],
[0,0,0,6,0,1,0,7,8],
[0,0,7,0,4,0,2,6,0],
[0,0,1,0,5,0,9,3,0],
[9,0,4,0,6,0,0,0,5],
[0,7,0,3,0,0,0,1,2],
[1,2,0,0,0,7,4,0,0],
[0,4,9,2,0,6,0,0,7],
]

def print_board(bo):
    """Will print the board list in a readable format"""

    #iterate through rows
    for i in range(len(bo)):
        #every third row (but not first row) print separator
        if i % 3 == 0 and i != 0:
            print("-------------------------")
        
        #iterate through columns (using length of, arbitrarily, the 1st row)
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="") #end="" means new line character wont be printed so line will continue
            
            #print each number
            if j != 8:
                print(str(bo[i][j]) + " ", end="") #print number then space, no new line
            else:
                print(str(bo[i][j])) #unless it's last number in row, then no space, yes new line

def find_empty(bo):
    """finds the first empty square from left to right, top to bottom"""

    #iterate through rows
    for i in range(len(bo)):
        #iterate through each column in row
        for j in range(len(bo[0])):
            #return cell if it's empty
            if bo[i][j] == 0:
                return (i, j)
            
    #if none are empty then puzzle solved
    return None