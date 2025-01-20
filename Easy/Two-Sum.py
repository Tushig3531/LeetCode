# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order. 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in hashmap and hashmap[comp] !=i:
                return [i, hashmap[comp]]
        return []
    
# In this code, For example "[2,7,11,15]". First we are creating hashmap which identifies the index of the array. 
# In this case 2-->0 7-->1 11-->2 15-->3. 