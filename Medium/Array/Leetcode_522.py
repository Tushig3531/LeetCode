# Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
# An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
# For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
# Example 1:
# Input: strs = ["aba","cdc","eae"]
# Output: 3
# Example 2:
# Input: strs = ["aaa","aaa","aa"]
# Output: -1


def findLUSlength(strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def is_subsequence(s,t):
            i=0
            for character in t:
                if i<len(s) and s[i]==character:
                    i+=1
                if i==len(s):
                    return True
            return i==len(s)
        strs.sort(key=len,reverse=True)
        for i in range(len(strs)):
            candidate=strs[i]
            # print(candidate)
            uncommon=True
            for j in range(len(strs)):
                if i!=j and is_subsequence(candidate,strs[j]):
                    uncommon=False
                    break
            if uncommon:
                return len(candidate)
        return -1
        
        
        
        
        
strs = ["aaa","aaa","aa"]
print(findLUSlength(strs))