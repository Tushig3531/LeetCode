# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1

def totalNQueens(n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(row,columns,diagnol_black,diagnol_white):
            if row==n:
                return 1
            result=0
            
            for column in range(n):
                if column in columns or (row-column) in diagnol_black or (row+column) in diagnol_white:
                    continue
                result+=backtrack(
                    row+1, columns|{column}, diagnol_black|{row-column}, diagnol_white|{row+column}
                )
            return result
        return backtrack(0,set(),set(),set())

                
        
n=4
print(totalNQueens(n))