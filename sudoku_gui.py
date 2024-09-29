#sudoku gui

import tkinter as tk #imports gui toolkit
from sudoku_solver import solve_sudoku #imports solve function

def create_grid():
    "Makes 9x9 sudoku board for players to input a value in each cell"
    
    entries=[] #2D that'll hold 9x9 Entry widgets

    #Make outer loop to create frames for each 3x3 box
    for box_row in range(3):
        for box_col in range(3):
            #make frame
            frame = tk.Frame(root, highlightbackground="black", highlightthickness=3)
            frame.grid(row=box_row*3, column=box_col*3, rowspan=3, columnspan=3)

            for row in range(3): #loops through each row

                #empty list that'll be the current row being made before its added to entries
                row_entries = [] 

                for col in range(3): #loops through each column

                    #creates Entry widget (input field) 3 wide, with centred text in 18pt Arial
                    entry = tk.Entry(frame, width=3, justify='center', font=('Arial', 18))
                    #place input field on GUI grid
                    entry.grid(row=row, column=col, padx=5, pady=5)
                    row_entries.append(entry) #adds current entry to current row
                
                entries.append(row_entries) #Adds completed row to entries 2D list

    return entries #returns 9x9 grid of input fields

def get_board(entries):
    """converts user inputs into 2D list"""
    board = []

    for row_entries in entries: #loops over each row of entries

        board_row = [] #empty list for current row

        for entry in row_entries: #loops over each entry of current row

            value = entry.get() #gets current value in Entry widget
            value = int(value) #convert to integer
            #if value is 1-9, save it as is, if not, save it as 0 (empty square)
            board_row.append(value if value.isdigit() else 0)
        
        board.append(board_row) #add row to board
    
    return board

#update_grid(board, entries)

#solve_sudoku_gui(entries):
    #board = get_board(entries)
    #solved_board = solve_sudoku(board)
    #if solved_board:
        #update_grid(solved_board, entries)
    #else:
        #show error message

root = tk.Tk() #make window
root.title("Sudoku Solver")

entries = create_grid()
#make instructional label here
#make solve button here
#maybe make solved/error messages here too


root.mainloop() #run event checker
