# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.
# Example 1:
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

def integerBreak(n):
        """
        :type n: int
        :rtype: int
        """
        dp={1:1}
        for num in range(2,n+1):
            dp[num]=0 if num==n else num
            for i in range(1,num):
                value=dp[i]*dp[num-i]
                dp[num]=max(dp[num],value)
        return dp[num]
        # def dfs(num):
        #     if num in dp:
        #         return dp[num]
        #     dp[num]=0 if num==n else num
        #     for i in range(1,num):
        #         value=dfs(i) * dfs(num-i)
        #         dp[num]=max(dp[num],value)
        #     return dp[num]
        # return dfs(n)
                
n=10
print(integerBreak(n))