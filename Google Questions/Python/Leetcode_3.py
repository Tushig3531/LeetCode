# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        char={} #this includes the list of chars
        result=0 #this is the end result
        start=0 #this is to track if the char is repeating and indicates where it should start
        for i in range(start,len(s)): #loop between the 0 to the end of the s. Each index will go as i
            if s[i] in char and char[s[i]]>=start: #if s's i-th index in char and the char's s's i-th element is bigger than start. Basically if it is not in the same place and s[i] in the char
                start=char[s[i]]+1 #start will move 1 index
            char[s[i]]=i #and our i-index will become char[s[i]]
            result=max(result,i-start+1) #in the end take the max of the result and the i-start+1 as result
        return result #then return it
        
s="abcabcbb"
print(lengthOfLongestSubstring(s))

#abcabcbb
#i=0-->a
#i=1-->b
#i=2-->c
#i=3 -->a because a's 3 is bigger than 0. a's index will become i=3
#a=3,b=1,c=1
#i=4 -->b because b's 4 is bigger than 1. b will become 4
#i=5 -->c because b's 5 is bigger than 2. c will become 5
#i=6 -->b, b will become 6
#i=7 -->b, b will become 7
#in the end our hash will look like: "{a:"3",b:"7",c:"5"}"
#in the end 5-3+1=3
#our result will become 3