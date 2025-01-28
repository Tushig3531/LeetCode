# Given an m x n matrix, return all elements of the matrix in spiral order.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        value=[]
        left, right=0, len(matrix[0])
        top, bottom=0, len(matrix)

        while right>left and top<bottom:     
            for top_column_left_to_right in range(left, right):
                value.append(matrix[top][top_column_left_to_right])
            top += 1
        
            for right_row_top_to_bottom in range(top, bottom):
                value.append(matrix[right_row_top_to_bottom][right-1])
            right -= 1

            if not (left<right and top<bottom): break
            
            for bottom_column_right_to_left in range(right-1, left-1,-1):
                value.append(matrix[bottom-1][bottom_column_right_to_left])
            bottom -= 1
            
            for left_row_bottom_to_top in range(bottom-1,top-1,-1):
                value.append(matrix[left_row_bottom_to_top][left])
            left += 1
        return value
    
# I solved it basically same as the Leetcode_59 which I did yesterday
