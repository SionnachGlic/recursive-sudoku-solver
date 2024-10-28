#sudoku gui

import tkinter as tk #imports gui toolkit
from sudoku_solver import solve_sudoku #imports solve function

def create_grid():
    "Makes 9x9 sudoku board for players to input a value in each cell"
    
    entries=[] #2D that'll hold 9x9 Entry widgets

    #make 9 rows
    for row in range(9):
        row_entries = [] #to hold current row of entries

        #make 9 columns
        for col in range(9):

            #make frame for each cell
            frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
            frame.grid(row=row, column=col, sticky="nsew")

            #make thicker border for 3x3 grid sections (not working yet)
            if row % 3 == 0:
                frame.grid(row=row, column=col, sticky="nsew", pady=(2,0))
            if col % 3 == 3:
                frame.grid(row=row, column=col, sticky="nsew", padx=(2,0))
            
            #greate Entry widget within each frame
            entry = tk.Entry(frame, width=3, justify='center', font=('Arial', 18))
            entry.pack(padx=5, pady=5)

            row_entries.append(entry) #add entry to current row

        entries.append(row_entries) #add current row to entries


    return entries #returns 9x9 grid of input fields

def get_board(entries):
    """converts user inputs into 2D list"""
    board = []

    for row_entries in entries: #loops over each row of entries

        board_row = [] #empty list for current row

        for entry in row_entries: #loops over each entry of current row

            value = entry.get() #gets current value in Entry widget
            #if value is 1-9, save it as is, if not, save it as 0 (empty square)
            board_row.append(int(value) if value.isdigit() else 0)
        
        board.append(board_row) #add row to board
    
    return board


def update_grid(board, entries):
    """Visually updates input grid with generated solution"""
    #iterate over each row
    for row in range(9):
        #within each row, iterate over each column (cell)
        for col in range(9):
            #delete current value
            entries[row][col].delete(0, tk.END)
            #insert value from solved board
            entries[row][col].insert(0, str(board[row][col]))


def solve_sudoku_gui(entries):
    board = get_board(entries)
    solved_board = solve_sudoku(board)

    #if sudoku solved, update it
    if solved_board:
        update_grid(solved_board, entries)
    else:
        #show error message
        tk.messagebox.showerror("No solution found!") #not working for some reason
 

root = tk.Tk() #make window
root.title("Sudoku Solver")

entries = create_grid()

#make instructional label here

#solve button
solve_button = tk.Button(root, text="Solve", command=lambda: solve_sudoku_gui(entries))
solve_button.grid(row=10, column=0, columnspan=9)

 

#maybe make some different solved/error messages here too when there's better error handling


root.mainloop() #run event checker
