# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.



class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
    
        n=len(haystack)
        # in sadbutsad --> n=8
        m=len(needle)
        # in sad --> m=2
        if n<m:
            return -1
        for i in range(n-m+1):
            # 8-2+1=7; for i in range(7): 0,1,2,3,4,5,6
            if haystack[i:i+m] == needle:
                # haystack[i:i+2]==needle
                # haystack[0:2]--> sad==needle
                # haystack[1:3]--> adb==needle
                # haystack[2:4]-->dbu==needle
                # haystack[3:5]-->but==needle
                # haystack[4:6]-->uts==needle
                # haystack[5:7]-->tsa==needle
                # haystack[6:8]-->sad==needle
                return i
        return -1
        
        