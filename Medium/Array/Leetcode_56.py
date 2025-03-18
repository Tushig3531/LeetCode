# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        result=[]
        for chunk in intervals:
            if not result or chunk[0]>result[-1][1]: #if result is empty or chunk's first index is bigger than the result's last element's last index
                result.append(list(chunk))
            else:
                result[-1][0]=min(result[-1][0],chunk[0])
                result[-1][1]=max(result[-1][1],chunk[1]) #else the result's last element's last index will the max of result's element's last index and chunk's last element
            
        
        return result
            
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))