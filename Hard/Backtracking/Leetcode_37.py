# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

def solveSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def valid(row,column,char):
            # Checking the column
            for j in range(9): #j-->012345678
                if board[row][j]==char: #if the board's row's j-th value is equal to char
                    return False # return false
            # Checking the row
            for i in range(9): # i-->012345678
                if board[i][column]==char: #if the board's column's i th value is equal to char
                    return False #return False
                
            # Checking the 3x3 boxes
            box_row_start=(row//3)*3 
            #creating small box grid for example row is 0,1,2,3,4,5,6,7,8. 0,1,2 are in one grid because (0,1,2//3)*3 is 0 and 3,4,5 are 1 and 6,7,8 are 2. 
            
            box_column_start=(column//3)*3 
            #creating small box grid for example column is 0,1,2,3,4,5,6,7,8. 0,1,2 are in one grid because (0,1,2//3)*3 is 0 and 3,4,5 are 1 and 6,7,8 are 2. 
            
            for i in range(box_row_start,box_row_start+3): #This loops in each small boxes
                for j in range(box_column_start,box_column_start+3):
                    if board[i][j]==char: #If the small box is equal to char
                        return False #return false
            return True #else return true
        
        def backtrack():
            for i in range(9): # i-->012345678
                for j in range(9): # j-->012345678
                    if board[i][j]==".": #if i and j the index is "."
                        for char in "123456789": #char-->1,2,3,4,5,6,7,8,9
                            if valid(i,j,char): # If it is passing the condition in valid function
                                board[i][j]=char # i-th and j-th index are become char
                                if backtrack():  # If backtrack function is done return True
                                    return True
                                board[i][j]="." # If "." still existing
                        return False #return False
            return True # In the end return True
        backtrack() #Recursion
                                    
                                
            
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)
for row in board:
    print(" ".join(row))
