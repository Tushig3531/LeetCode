# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

# Example 1:
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
# Example 2:
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1


def fourSumCount(nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        n=len(nums1)
        hashmap={}
        for i in range(n):
            for j in range(n):
                s=nums1[i]+nums2[j]
                if s in hashmap:
                    hashmap[s]+=1
                else:
                    hashmap[s]=1
                # print(hashmap)
        # print(hashmap)
        count=0
        for k in range(n):
            for l in range(n):
                t=nums3[k]+nums4[l]
                # print(t)
                addition=-t
                # print(addition)
                if addition in hashmap:
                    count+=hashmap[addition]
                    print(count)
                    # print(hashmap)
                # print(hashmap)
        # print(hashmap)
        return count
        
                
        
        
        
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(fourSumCount(nums1,nums2,nums3,nums4))
        