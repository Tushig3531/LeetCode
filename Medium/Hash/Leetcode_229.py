# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Example 1:
# Input: nums = [3,2,3]
# Output: [3]
# Example 2:
# Input: nums = [1]
# Output: [1]
# Example 3:
# Input: nums = [1,2]
# Output: [1,2]

def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap={}
        
        for num in nums:
                hashmap[num]=hashmap.get(num,0)+1
        # return hashmap
        result=[]
        condition=len(nums)//3
        # print(n)
        for num,count in hashmap.items():
                if count>condition:
                        result.append(num)
        return result
        
        
        
nums=[3,2]
print(majorityElement(nums))