# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.
# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:
# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
def isPowerOfThree(n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(x):
            if x==1:
                return True
            if x%3!=0 or x<=0:
                return False
            return helper(x//3)
        return helper(n)
            
        
n=9
print(isPowerOfThree(n))