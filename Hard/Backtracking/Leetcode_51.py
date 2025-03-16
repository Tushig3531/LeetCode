# # The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# # Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# # Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]

def solveNQueens(n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result=[]
        board=[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(".")
            board.append(row)
        
        def valid(board, row, col):
            
            for i in range(row):
                if board[i][col]=='Q':
                    return False
            i,j=row-1,col-1
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1

            i,j=row-1,col+1
            while i>=0 and j<n:
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1
            return True
        def backtrack(row):
            if row==n:
                temp=[]
                for r in board:
                    row_str="".join(r)
                    temp.append(row_str)
                result.append(temp)
            
            for col in range(n):
                if valid(board,row,col):
                    board[row][col]="Q"
                    backtrack(row+1)
                    board[row][col]="."
        backtrack(0)
        return result
                
n=4
print(solveNQueens(n))
        
