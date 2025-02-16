# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]

def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[[1]] #initial result, because it starts if 1
        for i in range(numRows-1): #because we took the first row it should start from the next one
                temporary=[0]+result[-1]+[0] #this is the temporary which add zero in the both side of array. For example: 1 2 1, then after we add 1+2, 1 3 3 1. It will be hard approach because it is hard to stay 1 in the place. So I am adding 0 in both side, so it will easier to have 1 in our next row. 1+0=1, 1 3 3 1
                row=[] #this is initializing the row
                for j in range(len(result[-1])+1): #this is the loop for getting the number
                        row.append(temporary[j]+temporary[j+1]) #appends the middle numbers to the row
                result.append(row) 
        return result
numRows=5
print(generate(numRows))