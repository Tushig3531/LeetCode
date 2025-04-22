# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order. 

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={} #too: index
        for i, n in enumerate(nums):
            zoruu=target-n
            if zoruu in hashmap:
                return [hashmap[zoruu],i]
            hashmap[n]=i
        return 
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))
# In this code, For example "[2,7,11,15]". First we are creating hashmap which identifies the index of the array. 
# In this case 2-->0 7-->1 11-->2 15-->3. Then I identified that adding two number is A+B=target, but we know that is "A"(because we are picking it first) and the target.
# So it will be B=target-A. Thus, I substracted A from target and searched B from the Array using if function. If B is in the Array it will give me the hashmap. If not it will return nothing.