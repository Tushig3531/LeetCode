# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group=defaultdict(list) 
        for i in strs:
            key=[0]*26
            for j in i:
                key[ord(j)-ord("a")]+=1
            key=tuple(key)
            group[key].append(i)
        return group.values()
        
strs = ["eat","tea","tan","ate","nat","bat"]       
print(groupAnagrams(strs))