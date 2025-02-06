# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]

def permute(nums):
    result=[]
    def backtrack(start):
        if start==len(nums):
            result.append(nums[:]) # returns when the length of the nums is equal to start. It should return the whole list
            return
        for i in range(start,len(nums)): #loops between start to length of the nums
            nums[start],nums[i]=nums[i],nums[start] #num's start index will be our nums' i-th index and the nums's i-th index will be our num's start index
            backtrack(start+1) #then start index will move by 1
            nums[start],nums[i]=nums[i],nums[start]  #Then repeat the process again. Oue nums' start index will become our nums' i-th index and our nums's i-th index will become our nums's start index
            
            #Basically this process is swapping those strings between " nums[start],nums[i]=nums[i],nums[start]"
    backtrack(0) #start will start from 0
    
    return result 
        

nums=[1,2,3]
print(permute(nums))