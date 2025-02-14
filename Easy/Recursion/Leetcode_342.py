# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.
# Example 1:
# Input: n = 16
# Output: true
# Example 2:
# Input: n = 5
# Output: false
# Example 3:
# Input: n = 1
# Output: true

def isPowerOfFour(n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(x):
            if x==1:
                return True
            if x<=0 or x%4!=0:
                return False
            return helper(x//4)
        return helper(n)
        
n=16
print(isPowerOfFour(n))