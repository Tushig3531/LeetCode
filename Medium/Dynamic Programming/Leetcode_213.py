# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:
# Input: nums = [1,2,3]
# Output: 3

def rob(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        def hulgai(houses):
            previous=0
            current=0
            for money in houses:
                previous,current=current,max(current,previous+money)
            return current
        beginning_to_end=hulgai(nums[1:])
        end_to_beginning=hulgai(nums[:-1])
        return max(beginning_to_end,end_to_beginning)
        
            
        
        
nums = [1,2,3,1]
print(rob(nums))