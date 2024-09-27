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

def valid_sudoku(bo, number, position):
    """Checks number is valid by standard sudoku rules
    (unique to row, column, and box)
    number is int in cell at given position tuple (row, column)"""

    #check each column in row
    for i in range(len(bo[0])): #0 is arbitrary since all rows have same length
       
        #check if number at position is equal to another in row
        #position is inputed tuple, position[0] is current row
        #pos[1] is current column, which shouldn't be checked as number will obvs be equal to itself
        if bo[position[0]][i] == number and position[1] != i:
            return False
    
    #check each row in column, same method as above
    for i in range(len(bo)):
        if bo[i][position[1]] == number and position[0] != i:
            return False
    
    #check box
    #identify which box by dividing position by 3
    #which box column
    box_x = position[1] // 3
    #which row
    box_y = position[0] // 3

    #check all cells in box
    #to get to correct index range multiple above values by 3
    #and add 3 because for loops don't check last value
    #iterate through the relevant rows
    for i in range(box_y*3, box_y*3 + 3):
        #iterate through the relevant columns within those rows
        for j in range(box_x*3, box_x*3 + 3):
            #check if number at position is equal
            if bo[i][j] == number and (i, j) != position:
                return False
    
    #if tests passed, it's valid, so return True
    return True



print_board(board)



            
