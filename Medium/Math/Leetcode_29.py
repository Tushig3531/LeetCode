# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.

def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        upper_bound=2**31-1
        lower_bound=-2**31
        if dividend == lower_bound and divisor == -1:
            return upper_bound
        if (dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
            
        output=0
        dividend=abs(dividend)
        divisor=abs(divisor)
        
        while dividend>=divisor: #10,3
            
            current = divisor #3
            times_added = 1
            while dividend >= (current + current): #10>=6
                current = current + current #current=6
                times_added = times_added + times_added #times_added=2
            dividend = dividend - current #dividend=4
            output = output + times_added #output=3
            
        if sign == -1:
            result = 0-output
        else:
            result = output
            
        if result > upper_bound:
            return upper_bound
        elif result < lower_bound:
            return lower_bound
        return result
        
    
print(divide(10,-3))