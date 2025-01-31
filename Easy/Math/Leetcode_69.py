# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        left=0
        right=x
        result=0
        
        while left<=right:
            median=left+((right-left)//2)
            if median**2>x:
                right=median-1
            elif median**2<x:
                left=median+1
                result=median
            else:
                return median
        return result
            
print(mySqrt(7))