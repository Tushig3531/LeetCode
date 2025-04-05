# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1


def uniquePathsWithObstacles(obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row=len(obstacleGrid)
        column=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[row-1][column-1]==1:
            return 0 #if the obstacle is in the end or start it should return 0
        dynamic=[]
        for _ in range(row):
            temp=[0]*column
            dynamic.append(temp)
            #making same size of matrix
        # print(dynamic)
        dynamic[0][0]=1 #making the start 1, because this is where we should start
        # print(dynamic)
        for i in range(row): #looping in each row
            for j in range(column): #and each column
                if obstacleGrid[i][j]==1: #if the obstacle occur
                    dynamic[i][j]=0 #it should become 0 because there is no way
                else:
                    if i>0: 
                        dynamic[i][j]+=dynamic[i-1][j] #if i is bigger than 0 which is 1, it should move bottom
                    if j>0:
                        dynamic[i][j]+=dynamic[i][j-1] #if j in 1, it should move right
        return dynamic[row-1][column-1] #it gives the last value of end point
        
    #basically the logic is:
    # [0,0,0]
    # [0,1,0]
    # [0,0,0] this is the beginning
    # then we made [0][0]==1
    # [1,0,0]
    # [0,1,0]
    # [0,0,0]
    # then if [i][j]==1 it will turn 0
    # [1,0,0]
    # [0,0,0]
    # [0,0,0]
    # then the function moves right or bottom while turning them into 1
    # [1,1,1]
    # [1,0,1]
    # [1,1,0]
    # in the end the 1+1 is 2 last index is 2
    # [1,1,1]
    # [1,0,1]
    # [1,1,2]
    # which we are returning
                   
        
obstacleGrid=[[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))