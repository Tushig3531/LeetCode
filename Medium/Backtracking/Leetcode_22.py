# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

def generateParenthesis(n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        parenthesis_container=[]
        def backtrack(open,closed):
            if open==closed==n: #rule1
                result.append("".join(parenthesis_container))
                return
            if open<n: #rule2
                parenthesis_container.append("(")
                backtrack(open+1, closed)
                parenthesis_container.pop()
            if closed<open: #rule3
                parenthesis_container.append(")")
                backtrack(open,closed+1)
                parenthesis_container.pop()
        backtrack(0,0)
        return result
            
print(generateParenthesis(3))

# In this code I used backtracking to find the possible variables of parenthesis. 
# To solve this problem there are 3 rules. 
# 1) open and closed parenthesis must be equal to n
# 2) add only open parenthesis when open is less than n
# 3) closed must be less than open, because we can not open the parenthesis with closing
# If the parenthesis pass the condition of rule1, all the parenthesis must be added in the parenthesis container and which must be added in result
# If the parenthesis pass the rule2, it will add open parenthesis. And the parenthesis container will take the open parenthesis. Then the function restarts
# If the parenthesis pass the rule3, it will add close parenthesis. And the parenthesis container will take the closed parenthesis. Then the fuction restarts
# The backtracking will start with open=0 and closed=0
# In the end it will return the result