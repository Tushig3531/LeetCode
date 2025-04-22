# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
# Example 1
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: tru
# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

def wordPattern(pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        hashmap={}
        reverse_hashmap={}
        i_values=[]
        j_values=[]
        for i in pattern:
            i_values.append(i)
        for j in s.split():
            j_values.append(j)
            
        if len(i_values)!=len(j_values):
            return False
            
        for key,value in zip(i_values,j_values):
            if key in hashmap:
                if hashmap[key]!=value:
                    return False
            else:
                if value in reverse_hashmap:
                    return False
                hashmap[key]=value
                reverse_hashmap[value]=key
        return True
                
        # print(hashmap)
                
        
pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern,s))
