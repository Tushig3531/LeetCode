# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

def minPathSum(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        if not grid[0]:
            return 0
        rows=len(grid)
        columns=len(grid[0])
        
        temp=[]
        for i in range(rows):
            row=[]
            for j in range(columns):
                row.append(0)
            temp.append(row)
        temp[0][0]=grid[0][0]
        
        for column in range(1,columns):
            temp[0][column]=temp[0][column-1]+grid[0][column]
            
        for row in range(1,rows):
            temp[row][0]=temp[row-1][0]+grid[row][0]
            
        for row in range(1,rows):
            for column in range(1,columns):
                temp[row][column]=min(temp[row-1][column],temp[row][column-1])+grid[row][column]
        return temp[rows-1][columns-1]
    
        
        
        
        
        
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))