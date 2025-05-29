# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        index=0
        while index<=j:
            if nums[index]==0:
                nums[i],nums[index]=nums[index],nums[i]
                i+=1
                index+=1
            elif nums[index]==2:
                nums[index],nums[j]=nums[j],nums[index]
                j-=1
            else:
                index+=1
        return nums

nums = [2,0,2,1,1,0]
print(sortColors(nums))