# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

def getRow(rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row=[1]
        for i in range(1,rowIndex+1):
            row.append(row[-1]*(rowIndex-i+1)//i)
        return row
        
    
rowIndex = 3
print(getRow(rowIndex))