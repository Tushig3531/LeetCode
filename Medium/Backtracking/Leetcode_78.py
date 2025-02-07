# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

def subsets(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def backtrack(start,combination):
            result.append(list(combination)) #The is no base case condition, it asked me to give the every combinations
            for i in range(start,len(nums)): #Loops from the start to the end of the end of the nums
                combination.append(nums[i]) #Takes the nums's i-th index
                backtrack(i+1,combination) #Recursively call the backtrack function, but we have to i+1, because after we take the i-th index values in the combinations we should move to the next starting position.
                combination.pop()#pops the afterwards values
        backtrack(0,[])
        return result
nums = [1,2,3]
print(subsets(nums))   
