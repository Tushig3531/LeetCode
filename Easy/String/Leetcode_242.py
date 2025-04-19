# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_s={}
        for i in s:
            hash_s[i]=hash_s.get(i,0)+1
        # return hash_s
        hash_t={}
        for j in t:
            hash_t[j]=hash_t.get(j,0)+1
        # return hash_t
        if hash_s==hash_t:
            return True
        return False        
        

s = "anagra"
t = "nagaram"
print(isAnagram(s,t))