# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d


def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=[] #this takes the result of the merged text
        max_length=max(len(word1),len(word2)) #length of word1 "abcd" is 4 and word2 is 2. So the max_length will be 4
        for i in range(max_length): # i=0,1,2,3
            if i<len(word1): # 0<4 so append "a", 1<4 so append "b", 2<4 so append the rest
                result.append(word1[i]) 
            if i<len(word2):# 0<2 so append "p", 1<2 so append "q", 2<2 is false so it will end here
                result.append(word2[i])
        return "".join(result) #turn the result list into str
    
        
word1 = "abcd"
word2 = "pq"
print(mergeAlternately(word1,word2))