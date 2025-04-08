# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:

# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []

def wordBreak(s, wordDict):
    cache={}
    wordset=set(wordDict)
    def backtrack(start):
        if len(s)==start:
            return [""]
        if start in cache:
            return cache[start]
        
        result=[]
        for i in range(start,len(s)):
            word=s[start:i+1]
            if word not in wordset:
                continue
            strings=backtrack(i+1)
            if not strings:
                continue
            for substring in strings:
                sentence=word
                if substring:
                    sentence += " "+substring
                result.append(sentence)
        cache[start]=result
        return result
    return backtrack(0)

                    
            
    
    
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(wordBreak(s,wordDict))