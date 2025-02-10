# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

def subsetsWithDup(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[] #init result
        nums.sort() #sorts it
        def backtrack(start, combination): #backtrack function
            
            result.append(list(combination)) # append the result because there are no base case, it is returning every element of combination
            for i in range(start,len(nums)): #loops between start to the end of the nums
                if i>start and nums[i]==nums[i-1]: #if starts is less then i and i-th elements is same as i-1-th element. Basically if it is overlapping 
                    continue #we will ignore it
                combination.append(nums[i]) #put it in the combination
                backtrack(i+1,combination) #then moves to the next by i+1
                combination.pop() #pops the over stack combinations, basically pops the not necessary ones
        backtrack(0,[]) #where the backtrack should start
        return result 
                
                
                
                
                
                
nums=[1,2,2]
print(subsetsWithDup(nums))