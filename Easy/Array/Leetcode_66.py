# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.≈
# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# # Thus, the result should be [1,0].

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)
        for i in range(n-1,-1,-1): # This for loops from the back of the array: For example: if the array is [4,3,2,1], this will make the index read from the back like [1,2,3,4]
            if digits[i]<9: #if the index are less than 9
                digits[i]=digits[i]+1 #it will add 1
                return digits #and return the number
            digits[i]=0 #else the index will become zero and moves to the next index
        return [1]+digits #if there isn't any next index for example 9. It will add 1 in the array
    
    # With this, [4,3,2,1] will become [1,2,3,4] because 1 is less than 9, it will just add 1 in it. Ans [2,2,3,4]≈[4,3,2,2]
    # If the array is [4,3,2,9], it will become [9,2,3,4]. Because the index is 9, it will turn into 0 and move to the next index. So the next index "2" is less than 9 so it will just add 1. In the end, it will become [0,3,3,4] which means [4,3,3,0]