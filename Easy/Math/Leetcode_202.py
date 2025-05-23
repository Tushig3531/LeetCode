# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:
# Input: n = 2
# Output: false

def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        # boldoo=str(n)
        # result=0
        # for i in boldoo:
        #     digit=int(i)
        #     square=digit*digit
        #     result+=square
        # return result
        def recursive(current,used):
            if current==1:
                return True
            if current in used:
                return False
            used.add(current)
            result=0
            current_str=str(current)
            for i in current_str:
                digit=int(i)
                square=digit**2
                result+=square
            return recursive(result,used)
        return recursive(n,set())
                
            
            
        
        
n = 19
print(isHappy(n))