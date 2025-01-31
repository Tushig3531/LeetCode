# Given a string s, return the longest 
# palindromic
# substring
#  in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        start=0
        end=0
        n=len(s)
        
        for i in range(n):
            left=i  #This is for checking the odd number palindromes
            right=i
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            length1=right-left-1
            
            left=i  #This is for checking the even number palindromes
            right=i+1
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            length2=right-left-1
            
            max_length=max(length1, length2) #This takes the maximum length
            if max_length>end-start:
                start=i-(max_length-1)//2
                end=i+max_length//2
        return s[start:end+1]
        
    
print(longestPalindrome("ababd"))

# For example "ababd"
# First it makes it 1a 2b 3a 4b 5d
# Then the left=0 and right=0, (checking the odd number palindrome)
# ababd, index=0 is both "a", they are matching, then left-1 and right+1. But 0-1=-1 left is out of bound. So moves to the next index. 
# ababd, index=1 is both "b", they are matching, then left-1 and right+1. left is "a" and right is "a" they are both matching. Repeat the process, however left will be out of bound. "Current length=2-0-1=1"
# Then moves to the next index, index=2, they are both "a", repeat the process. Then they will get "bab" because "a" is not equal to "d". "Current length=3-1-2=0"
# 

# Now lets check the even number palindrome:
# Mostly same thing but right is starting from the next index: left=0 and right=1
# ababd, index=0, left is "a" and right is "b". "a" and "b" are not matching so next index.
# Keep repeats the process. But there is no even number palindrome.

# Eventually calculates the max length out of current length.
# But as long as it is giving me the only the length, but we need to return the string. So I implemented start and end point which reads the initial string. 
# As long as out max length is 1 and it found in index=1. start will become 1-(1-1)//2=1, index=1 and the end will become 1+3//2=2, index 2. 
# Eventually return index 1-3 which is bab


            
            
        
        
        