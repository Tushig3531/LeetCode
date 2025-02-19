# A happy string is a string that:
# consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
# Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
# Example 1:
# Input: n = 1, k = 3
# Output: "c"
# Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
# Example 2:
# Input: n = 1, k = 4
# Output: ""
# Explanation: There are only 3 happy strings of length 1.
# Example 3:
# Input: n = 3, k = 9
# Output: "cab"
# Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

def getHappyString(n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result=[] #init result
        input_char="abc" #base chars
        if n<=0: #n out of range
            return ""
        
        def backtrack(combination): #I am only using combination because I only need the combinations of the char, and if it is not repeating I do not need to check the start, it can start from everywhere 
            if len(combination)==n: #if the item in the combination touch the limit of n
                result.append("".join(combination)) #append
                return
         
            for char in input_char: #looping in the char
                if combination and combination[-1]==char: #if the appending char and previous char are same
                    continue #do not include it
                combination.append(char) #append the char in the combination
                backtrack(combination) #recursively calling
                combination.pop() #popping the overflow
        backtrack([]) #init 
        if k<=len(result): #because I am appending char in result for n amount, if the length of bigger than k. Which passing our condition.
            return result[k-1] #we should return the k'th item
        else:
            return "" #else empty
                    
                    
                        
                 
            
n = 1
k = 4

print(getHappyString(n,k))