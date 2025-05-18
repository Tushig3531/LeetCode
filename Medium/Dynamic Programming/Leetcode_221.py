# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:
# Input: matrix = [["0"]]
# Output: 0

def maximalSquare(matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_side=0
        x=len(matrix)
        y=len(matrix[0])
        dynamic=[]
        for i in range(x+1):
            row=[]
            for j in range(y+1):
                row.append(0)
            dynamic.append(row)
        for i in range(1,x+1):
            for j in range(1,y+1):
                if str(matrix[i-1][j-1])=='1':
                    dynamic[i][j]=1+min(dynamic[i-1][j],dynamic[i][j-1],dynamic[i-1][j-1]) #from this if the maktrix's matrix[i-1][j-1] is "1", so our "dynamic[i][j]" will be also 1, and min of (dynamic[i-1][j],dynamic[i][j-1],dynamic[i-1][j-1]) all have to 1 to create square, if any of them is 0 it will return 0 in that case it will not be square and ignore and moves to the next index. 
                    # print(dynamic[i][j])
                    max_side=max(max_side,dynamic[i][j]) #then it takes the max of the side
        return max_side*max_side #to create square we will need to multiply by itself
                
        
        
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))