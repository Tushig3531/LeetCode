# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

 

# Example 1:

# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:

# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

def nthUglyNumber(n):
        """
        :type n: int
        :rtype: int
        """
        ugly=[0]*n
        ugly[0]=1
        index_2=index_3=index_5=0
        next_2,next_3,next_5=2,3,5 
        for i in range(1,n):
            next_ugly=min(next_2,next_3,next_5)
            ugly[i]=next_ugly
            if next_ugly==next_2:
                index_2+=1
                next_2=ugly[index_2]*2
            if next_ugly==next_3:
                index_3+=1
                next_3=ugly[index_3]*3
            if next_ugly==next_5:
                index_5+=1
                next_5=ugly[index_5]*5
        return ugly[-1]
        
        
n=10
print(nthUglyNumber(n))