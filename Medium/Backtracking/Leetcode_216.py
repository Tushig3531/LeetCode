# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# Example 3:
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.


def combinationSum3(k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        possible_integer=[1,2,3,4,5,6,7,8,9]
        result=[]
        def backtrack(remain,combination,start):
            if remain==0 and len(combination)==k: #base case of where it should end
                result.append(list(combination))
                return
            if remain<0 and len(combination)>k: #base case of what it should ignore
                return
            for i in range(start,len(possible_integer)): #loops between start to the end of the possible_integer
                if i>start and possible_integer[i]==possible_integer[i-1]: #it should not repeat
                    continue #it it repeats ignore
                combination.append(possible_integer[i]) #append
                
                backtrack(remain-possible_integer[i],combination,i+1) #recursively call the function
                combination.pop() #pops the after values, over flow
        backtrack(n,[],0) #init
        return result
                
                
             
k=3
n=7
print(combinationSum3(k,n))







