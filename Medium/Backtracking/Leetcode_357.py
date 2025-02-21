# Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.
# Example 1:
# Input: n = 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
# Example 2:
# Input: n = 0
# Output: 1

def countNumbersWithUniqueDigits(n):
        """
        :type n: int
        :rtype: int
        """
        result=[]
        if n==0:
            return 1
        digits = [str(i) for i in range(10)]
        result=[]
        
        def backtrack(combination):
            if combination:
                result.append(int("".join(combination)))
            if len(combination)==n:
                return
            for digit in digits:
                if digit in combination:
                    continue
                if not combination and digit=='0':
                    continue
                combination.append(digit)
                backtrack(combination)
                combination.pop()
        if 0 not in result:
            result.append(0)
        backtrack([])
        return len(result)
        
        
n=3
print(countNumbersWithUniqueDigits(n))