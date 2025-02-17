# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]

def partition(s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result=[]
        def backtrack(start,combination):
            if start==len(s): #if start is equal to length of s, which means when it ends
                result.append(list(combination)) #append it to result
                return
            for i in range(start,len(s)): #from 0 to the end of the lenght of s
                if s[start:i+1]==s[start:i+1][::-1]: #if s's start to i+1 is equal to reverse
                    combination.append(s[start:i+1]) #append it to the combination
                    backtrack(i+1,combination) #it should start from the next index
                    combination.pop() #pop the overflow
        backtrack(0,[])
        return result
            
s="aab"
print(partition(s))

# aab
# 