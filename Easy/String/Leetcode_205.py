# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap_index={}
        hashmap_count={}
        for i,char in zip(s,t):
            if i in hashmap_index:
                if hashmap_index[i]!=char:
                    return False
            else:
                if char in hashmap_count:
                    return False
                hashmap_index[i]=char
                hashmap_count[char]=i
        return True                
            

s = "egg"
t = "add"
print(isIsomorphic(s,t))