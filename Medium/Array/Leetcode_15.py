# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() #it sorts the nums
        n=len(nums) 
        target=0 #setting the target
        result=[] #result list
        for i in range(n-2): #loop between n-2'th index
            if i > 0 and nums[i] == nums[i-1]:  #if the i is greater than 0 and the nums i-th index and i-1-th index are equal
                continue #do not include the duplicated values
            left=i+1 #left index init
            right=n-1 #right index init
            while left<right: #if the left is less than right
                current_sum=nums[i]+nums[left]+nums[right] #sum of the indexes
                if current_sum ==target: #base case
                    result.append([nums[i],nums[left],nums[right]]) #append the value in the list
                    while left<right and nums[left]==nums[left+1]: #if the left is less than the right and nums of left and left+1 are equal
                        left+=1 #left moves to the next index which avoid the duplicates
                    left+=1 #then moves left moves to the left+1
                    right-=1 #and right moves back by 1
                elif current_sum<target: #if sum is less then the target left will move by 1
                    left+=1
                else:
                    right-=1 #if current is greater than the target, right will move down by 1
        return result 
nums=[-1,0,1,2,-1,-4]
print(threeSum(nums))
                    
                    
                
        