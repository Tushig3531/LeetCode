# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.
# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

def longestPalindrome(s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={}
        for ch in s:
            hashmap[ch]=hashmap.get(ch,0)+1
        # return hashmap
        sum_even=0
        max_odd=0
        for count in hashmap.values():
            if count%2==0:
                sum_even+=count
            else:
                sum_even+=count-1
                max_odd=1
                
        return sum_even+max_odd
        
        
s = "abccccddA"
print(longestPalindrome(s))     
