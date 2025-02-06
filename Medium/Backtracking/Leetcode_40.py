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
        candidates.sort() #sort the candidates
        result=[]
        def backtrack(remain,combination,start): #The concept is If I substract the index from the remaining over and over again it will give me the whole combinations of the candidates
            if remain==0:
                result.append(list(combination)) #list those combinations
                return
            if remain<0: #If the remaining is still bigger than the remaining it should loop the process again
                return
            for i in range(start,len(candidates)): #loop between the 0 to the length of the candidates
                if i > start and candidates[i] == candidates[i - 1]: #If the index is bigger than the start and the i-th candidate is equal to i-1-th candidate
                    continue #it should continue
                combination.append(candidates[i]) #else, put those candidates in the combination list
                backtrack(remain-candidates[i],combination,i+1) #Then it changes the remaining, and recursively. i+1 means it can not take the same value. 
                combination.pop() #takes the combinations
        backtrack(target,[],0) #Where it should start
        return result #result
                    
                
            
            
            
candidates=[2,5,2,1,2]
target=5
print(combinationSum2(candidates,target))
