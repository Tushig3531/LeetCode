# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:
# Input: nums = [1], target = 1
# Output: 1

def findTargetSumWays(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo={}
        if not nums:
            return 0
        def backtrack(start,current):
            if start==len(nums):
                if current==target:
                    return 1
                return 0
            
            if (start,current) in memo:
                return memo[(start,current)]
            
            add=backtrack(start+1,current+nums[start])
            substract=backtrack(start+1,current-nums[start])
            memo[(start,current)]=add+substract
            return memo[(start,current)]
        return backtrack(0,0)
                
                    
                
        
        
nums = [25,14,16,44,9,22,15,27,23,10,41,25,14,35,28,47,39,26,11,38]
target = 43
print(findTargetSumWays(nums,target))