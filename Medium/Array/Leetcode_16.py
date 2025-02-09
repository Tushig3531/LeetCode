# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 
 
def threeSumClosest(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        closed_sum=float('inf') #initializing the closed_sum to large numbers
# The rest process is kinda similar to leetcode_15 but.
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                current_sum=nums[i]+nums[left]+nums[right]
                if abs(current_sum-target)<abs(closed_sum-target): #When the current target minus target is less than clused_sum minus target current sum will be our closed sum.
                    closed_sum=current_sum
                if current_sum<target:
                    left+=1
                elif current_sum>target:
                    right-=1
                else:
                    return current_sum
        return closed_sum
                    
nums=[-1,2,1,-4,10]
target=7

print(threeSumClosest(nums,target))
        
        