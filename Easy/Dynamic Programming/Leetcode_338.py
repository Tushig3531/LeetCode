# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

def countBits(n):
        """
        :type n: int
        :rtype: List[int]
        """
        # result=[]
        # for i in range(1,n+1):
            # print(i)
        dynamic=[0]*(n+1)
        # print(dynamic)
        for i in range(1,n+1):
            dynamic[i]=dynamic[i&(i-1)]+1
        return dynamic
            
        
        
n = 5
print(countBits(n))