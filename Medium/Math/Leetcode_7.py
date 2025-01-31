# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result=0
        lower_border=-2**31
        upper_border=2**31 -1
        if x>=0:
            sign=1
        else: 
            sign=-1
        x=abs(x)
        while x>0:
            result = result*10+x%10 
            x=x//10
        if result>upper_border or result<lower_border:
            return 0

        return result*sign
    
    # For example lets take numer 321. This algorithm will continue until x become less than 0. The initial result=0, so it will be result=0*10+321%10: So the first result will become 1. Then 321//10≈32. 32 is bigger than 0 so it repeats the process. Over and over again. The result will become 123. Then the sign, if the number is equal or bigger than 0 sign is 1, else -1. Then it will check the bound, if number is out of bound it will retunr 0 instead result*sign.
    # 321 is in the bound and result=123 and sign=1//123*1=123. 
    # Final answer 123
    

