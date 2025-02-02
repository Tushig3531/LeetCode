# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 1
        step = [0]*(n+1) #number of steps
        step[0] = 1 #base case
        step[1] = 1 #base case

        for i in range(2,n+1):
            step[i] = step[i-1] + step[i-2] #to step i, we can come from step i-1 or from i-2. Because we are only travelling with 1 and 2
        return step[n]
        
            
