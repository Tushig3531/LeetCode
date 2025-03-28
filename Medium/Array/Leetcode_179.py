# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.


# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"

def largestNumber(nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums_str=[]
        for num in nums:
            nums_str.append(str(num))
        # print(nums_str)
        
        max_len=0
        for s in nums_str:
            current=len(s)
            if current>max_len:
                max_len=current
        def sort_key(s):
            return s*max_len
        sorted_list=sorted(nums_str,key=sort_key,reverse=True)
        if sorted_list[0] == "0":
            result = "0"
        # print(sorted_list)
        else:
            result="".join(sorted_list)
        return result
        
        
        # def sort_key(s):
        #     first_digit=int(s[0])
        #     # print(first_digit)
        #     remainder=0
        #     if len(s)>1:
        #         remainder=int(s[1:])
        #     else: first_digit
        #     return (-first_digit,-remainder)

        # sorted_list=sorted(nums_str,key=sort_key)
        # print(sorted_list)
        # result="".join(sorted_list)
        # return result
        
nums = [0,0]
print(largestNumber(nums))
        