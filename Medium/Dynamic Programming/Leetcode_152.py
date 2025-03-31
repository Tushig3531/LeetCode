# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ehleh=nums[0]
        duusah=nums[0]
        etses=nums[0]
        for too in nums[1:]:
            if too<0:
                duusah,ehleh=ehleh,duusah
                
            duusah=max(too,duusah*too)
            ehleh=min(too,ehleh*too)
            etses=max(etses,duusah)
            
        return etses
        
nums = [2,3,-2,4]
print(maxProduct(nums))