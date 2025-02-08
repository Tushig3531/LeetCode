# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


def exist(board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, columns=len(board),len(board[0]) #determining how many rows and columns of row and column
        path=set() #making the path set
        def backtrack(r,c,i): 
            if i==len(word): #base case, if the i is equal to the length of the word
                return True 
            #checking the boundary
            if (r<0 or c<0  #if the row and column are less than 0
                or r>=rows or c>=columns #if the row and column are out of the boundary of rows and columns of the board
                or word[i]!=board[r][c] #the word's i-th character is not matching with board's value in row and column
                or (r,c) in path): #or the value is already in the path
                return False
            path.add((r,c)) #add those characters in the path
            result=(backtrack(r+1,c,i+1) #recursively moves to the next index with row+1
                    or backtrack(r-1,c,i+1) #recursively moves to the next index with row-1
                    or backtrack(r,c+1,i+1) #recursively moves to the next index with column+1
                    or backtrack(r,c-1,i+1)) #recursively moves to the next index with column-1
            path.remove((r,c)) #removes the current cell from the path
            return result
        for row in range(rows): #loop in every row of rows
            for column in range(columns): #loo in every column in columns
                if backtrack(row,column,0): return True #if backtrack return True, return True
        return False #else False
                
                
                
            
        
        
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCCED"
print(exist(board,word))
        