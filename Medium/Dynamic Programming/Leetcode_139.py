# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

def wordBreak(s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordset=set(wordDict) #{'leet', 'code'}
        # print(wordset)
        temp={} #init set
        def dn(start): #calling function for dynamic programming
            if start==len(s): #this means when start reaches the end, and if so it should be successful
                return True
            if start in temp: #checks if the result for the current start index has already been computed
                return temp[start] #if it has, then returns that stored result
            for i in range(start+1,len(s)+1): #looping from 1 to the end of the string
                # print(s[start:i])
                if s[start:i] in wordset and dn(i): #l, le, lee, leet, c, co, cod, code in the wordset
                    temp[start]=True #turn the stored result to True
                    return True #then True
            temp[start]=False #if it is not stroed False
            return False
        return dn(0) #init start
                                    
        
s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s,wordDict))