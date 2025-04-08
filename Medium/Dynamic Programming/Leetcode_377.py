# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0

def combinationSum4(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dynamic=[0]*(target+1)
        # print(dynamic)
        dynamic[0]=1
        # print(dynamic)
        for i in range(1,target+1):
            # print(i)
            # print(dynamic[i])
            for num in nums:
                # print(i)
                # print(dynamic[i])
                # 011,012,023,046
                print(num)
                if i>=num: 
                    # print(dynamic[i])
                    dynamic[i]+=dynamic[i-num]
        return dynamic[target]
        
        #i=1
        #i=1, num=1,2,3 when i==1 and num==1 dynamic[i]--> dynamic[1]+=dynamic[1-1], otherwise 2 and 3 are bigger than 1
        # dynamic[1]-->dynamic[0]+dynamic[1]
        # [1,0,0,0,0]-->[1,1,0,0,0] 
        
        # i=2
        # 2>1 2>=2 2<3, when num==1, dynamic[2]=dynamic[2]+dynamic[1], dynamic[2]==1
        # [1,1,1,0,0] , when num==2, dynamic[2]=dynamic[2]+dynamic[0], dynamic[2]==2
        # [1,1,2,0,0]
        
        # i=3
        # i is greater and equal to the all num, when num==1, dynamic[3]=dynamic[3]+dynamic[3-1], dynamic[3]==2
        # when num==2, dynamic[3]=2+dynamic[3-2] --> dynamic[3]=3
        # when num==3, dynamic[3]=3+dynamic[0] --> dynamic[3]=4
        # [1,1,2,4,0]
        
        # i=4
        # when num==1, dynamic[4]=0+dynamic[3],dynamic[4]=4
        # when num==2, dynamic[4]=4+dynamic[4-2], dynamic[4]=6
        # when num==3, dynamic[4]=6+dynamic[1], dynamic[4]=7
        # [1,1,2,4,7]
        
        # In the end it is returning the value of target, dynamic[target]-->dynamic[4]-->7
                    
            
        
nums = [1,2,3]
target = 4
print(combinationSum4(nums,target))