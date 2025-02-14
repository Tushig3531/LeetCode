# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

def myPow(x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x,n):
            if n==0:
                return 1
            if x==0:
                return 0
            result=helper(x,n//2)
            result=result*result
            if n%2:
                return result*x
            else:
                return result
        result=helper(x,abs(n)) 
        if n>0:
            return result
        else:
            return 1/result
        
        
        
x=2.00000
n=10
print(myPow(x,n))