# # Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# # Each number in candidates may only be used once in the combination.
# # Note: The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]


def combinationSum2(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result=[]
        def backtrack(remain,combination,start):
            if remain==0:
                result.append(list(combination))
                return
            if remain<0:
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                backtrack(remain-candidates[i],combination,i+1)
                combination.pop()
        backtrack(target,[],0)
        return result
                    
                
            
            
            
candidates=[2,5,2,1,2]
target=5
print(combinationSum2(candidates,target))
