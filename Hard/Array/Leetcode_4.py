# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_array = arr[:mid]
                right_array = arr[mid:]
                
                # Recursion
                merge_sort(left_array)
                merge_sort(right_array)
                
                # Merge the sorted halves
                i = j = k = 0
                while i < len(left_array) and j < len(right_array):
                    if left_array[i] < right_array[j]:
                        arr[k] = left_array[i]
                        i += 1
                    else:
                        arr[k] = right_array[j]
                        j += 1
                    k += 1
                
                
                while i < len(left_array):
                    arr[k] = left_array[i]
                    i += 1
                    k += 1
                
                
                while j < len(right_array):
                    arr[k] = right_array[j]
                    j += 1
                    k += 1

        def find_median(arr):
            print(f"Sorted Array: {arr}")  
            n = len(arr)
            mid = n // 2
            if n % 2 == 1:
                return arr[mid]
            else:
                return (arr[mid - 1] + arr[mid]) / 2

        
        merged_arr = nums1 + nums2
        merge_sort(merged_arr)
        print(f"Merged Array Before Finding Median: {merged_arr}")
        
        
        return find_median(merged_arr)

# Example Usage
solution = Solution()
print("Median 1:", solution.findMedianSortedArrays([1, 3], [2])) 
print("Median 2:", solution.findMedianSortedArrays([1, 2], [3, 4])) 
