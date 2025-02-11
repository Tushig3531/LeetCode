# An n-bit gray code sequence is a sequence of 2n integers where:

# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

 

# Example 1:
# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit
# Example 2:

# Input: n = 1
# Output: [0,1]

def grayCode(n):
        """
        :type n: int
        :rtype: List[int]
        """
        def power_of_2(x):
            result=1
            for _ in range(x):
                result*=2
            return result

        def bit(a,b):
            x=a^b
            return x and (x&(x-1))==0

        def backtrack(num, path):
            if len(path)==power_of_2(n):
                if bit(path[0],path[-1]):
                    return path
                return
            
            for i in range(n):
                next_num = num^power_of_2(i) 
                if next_num not in visited:
                    visited.add(next_num)
                    path.append(next_num)
                    result = backtrack(next_num, path)
                    if result:  
                        return result
                    path.pop() 
                    visited.remove(next_num)
            return
        visited={0}
        return backtrack(0,[0])
                
            
            
n=2
print(grayCode(n))
        
