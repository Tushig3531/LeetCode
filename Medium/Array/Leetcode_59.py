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
            # [
            #     [0, 0, 0, 0],
            #     [0, 0, 0, 0],
            #     [0, 0, 0, 0],
            #     [0, 0, 0, 0]
            # ]
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


# In this code here is the illustration:
#  L_________R
# |1   2  3  4|T
# |12 13 14  5|
# |11 16 15  6|
# |10  9  8  7|B
#  ------------
# I used 4 pointers left, right, top, bottom
#  L_________R
# |0   0  0  0|T
# |0   0  0  0|
# |0   0  0  0|
# |0   0  0  0|B
#  ------------
# First it will go left to right for n times, and using for loop I gave the 1,2,3,4 values in top=0 row
# After that I change the row of top with 1 so i will look like this:
#  L_________R
# |1   2  3  4|
# |0   0  0  0|T
# |0   0  0  0|
# |0   0  0  0|B
#  ------------
# Then I used for loop in right row and top to bottom: 5,6,7. And right will decrease index by 1.
#  L______R___
# |1   2  3  4|
# |0   0  0  5|T
# |0   0  0  6|
# |0   0  0  7|B
#  ------------
# Then I used for loop again but reversely until right to left-1. Thus it will give me 10,9,8. And decreased the index of bottom by 1.
#  L______R___
# |1   2  3  4|
# |0   0  0  5|T
# |0   0  0  6|B
# |10  9  8  7|
#  ------------
# Then I used for loop reversely until in left column bottom to top. 11,12. And increased the index of left will increase by 1.
#  ____L__R___
# |1   2  3  4|
# |12  0  0  5|T
# |11  0  0  6|B
# |10  9  8  7|
#  ------------
# As you can see, left right top and bottom are in same position as in the beginning. Thus it repeats the processes again. Until we get this.
#  ____L__R___
# |1   2  3  4|
# |12 13 14  5|T
# |11 16 15  6|B
# |10  9  8  7|
#  ------------
# But as I said in the code, left is increasing the index, right is decreasing, Top is increasing, bottom is decreasing. So it will give me this.
#  ____R__L___
# |1   2  3  4|
# |12 13 14  5|B
# |11 16 15  6|T
# |10  9  8  7|
#  ------------
# That will be the end of our code. So I used until the placement of Right and Left will be switched. 
