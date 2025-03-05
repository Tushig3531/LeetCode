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
        group=defaultdict(list) #this is the init group list dictionary
        for i in strs: #looping until the strs are finished
            key=[0]*26 #because of english letter has 26 letters, it must be one of them
            for j in i: #then looping the each i, for example, "eat --> e,a,t"
                key[ord(j)-ord("a")]+=1 #1) key[4]+1-->5
                # 2) key[0]+1-->1
                #3) key[19]+1-->20
                #This function identifies the key of the char's position
            key=tuple(key) #key-->[5,1,20]
            group[key].append(i) #and then append the keys in the key list of the group
        return group.values() #and return the value of it. 
        
strs = ["eat","tea","tan","ate","nat","bat"]       
print(groupAnagrams(strs))

