# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:
# Input: n = 1
# Output: [[1]]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix=[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(0)
            matrix.append(row)
            # which basically makes if n is equal to 4
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        left=0
        right=n-1
        top=0
        bottom=n-1
        value=1
        while left <=right:
            for column_top_left_to_right in range(left, right+1):
                matrix[top][column_top_left_to_right]=value
                value=value+1
            top=top+1

            for row_right_top_to_bottom in range(top,bottom+1):
                matrix[row_right_top_to_bottom][right]=value
                value=value+1
            right=right-1

            for column_bottom_right_to_left in range(right,left-1,-1):
                matrix[bottom][column_bottom_right_to_left]=value
                value=value+1
            bottom=bottom-1

            for row_left_bottom_to_top in range(bottom, top-1, -1):
                matrix[row_left_bottom_to_top][left]=value
                value=value+1
            left=left+1
        return matrix


# 