# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        rule=len(nums)//2
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
            # print(hashmap)
            if hashmap[num]>rule:
                return num
        return None
        
            
            
        
        
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))