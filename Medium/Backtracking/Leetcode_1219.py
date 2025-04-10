# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

# Return the maximum amount of gold you can collect under the conditions:
# Every time you are located in a cell you will collect all the gold in that cell.
# From your position, you can walk one step to the left, right, up, or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.
# Example 1:
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.
# Example 2:
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

def getMaximumGold(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        rows=len(grid)
        columns=len(grid[0])
        result=0
        def backtrack(i,j):
            if i<0 or i>=rows or j<0 or j>=columns or grid[i][j]==0:
                return 0
            temp=grid[i][j]
            grid[i][j]=0
            down=backtrack(i-1,j)
            up=backtrack(i+1,j)
            left=backtrack(i,j+1)
            right=backtrack(i,j-1)
            max_of_rows_columns=max(down,up,left,right)
            grid[i][j]=temp
            return temp+max_of_rows_columns
        for x in range(rows):
            for y in range(columns):
                if grid[x][y]!=0:
                    result=max(result,backtrack(x,y))
        return result
            
        
grid = [[0,6,0],[5,8,7],[0,9,0]]
print(getMaximumGold(grid))