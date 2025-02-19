def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        def backtrack(remain,combination,index_combination,start):
            if remain==0 and len(index_combination)==2:
                result.append((list(combination),list(index_combination)))
                return
            if len(index_combination)>=2:
                return
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                combination.append(nums[i])
                index_combination.append(i)
                backtrack(remain-nums[i],combination,index_combination,i+1)
                combination.pop()
                index_combination.pop()
        backtrack(target,[],[],0)
        for y in result:
            return y[1]
nums=[1,2,3,5,6]
target=4
print(twoSum(nums,target))