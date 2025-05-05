# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        # return hashmap
        max_length=0
        for num in hashmap:
            if num-1 not in hashmap:
                length=1
                while num+length in hashmap:
                    length+=1
                max_length=max(max_length,length)
                
        return max_length
        
# nums = [0,3,7,2,5,8,4,6,0,1]
# print(longestConsecutive(nums))
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))