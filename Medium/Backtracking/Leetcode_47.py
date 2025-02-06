# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def permuteUnique(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        def backtrack(remain,combination):
            if not remain: #if remain is empty
                result.append(combination) #take the combination
                return
            for i in range(len(remain)): #basically for looping the nums
                if i>0 and remain[i]==remain[i-1]: #if the index is less than 0 and remain's i-th index is equal to remain's i-1'th index
                    continue #skip it. Basically, if the number is already listed, it can not take that value. Instead it will skip it
                new_remain=remain[:i]+remain[i+1:] #the new_remain aka new nums will become. The numbers till the i-th index of remain + number from i+1'th index to end of the remain 
                backtrack(new_remain,combination+[remain[i]]) #recursion, changes the remaining with new_remain and the combination will take the remain's i-th index that we took.
                
        backtrack(nums,[]) #init
        return result
            
nums=[1,1,2]
print(permuteUnique(nums))