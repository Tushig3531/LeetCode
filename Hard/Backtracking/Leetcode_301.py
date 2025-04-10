# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

# Example 1:
# Input: s = "()())()"
# Output: ["(())()","()()()"]
# Example 2:
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
# Example 3:
# Input: s = ")("
# Output: [""]

def removeInvalidParentheses(s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=set()
        left_remain=0
        right_remain=0
        for i in s:
            if i=="(":
                left_remain+=1
            elif i==")":
                if left_remain>0:
                    left_remain-=1
                else:
                    right_remain+=1
        def backtrack(start,left,right,open_count,combination):
            if start==len(s):
                if left==0 and right==0 and open_count==0:
                    result.add(combination)
                return

            index=s[start]
            if index=='(' and left>0:
                backtrack(start+1,left-1,right,open_count,combination)
            if index==')' and right>0:
                backtrack(start+1,left,right-1,open_count,combination)
            
            path=combination+index
            if index=="(":
                backtrack(start+1,left,right,open_count+1,path)
            elif index==")":
                if open_count>0:
                    backtrack(start+1,left,right,open_count-1,path)
            else:
                backtrack(start+1,left,right,open_count,path)
        backtrack(0,left_remain,right_remain,0,"")
        return list(result)
        


        
        # total_left=s.count("(")
        # total_right=s.count(")")
        # total_pairs=min(total_left,total_right)
        # left=total_left-total_pairs
        # right=total_right-total_pairs
        
        # def backtrack(start,left,right,open_count,combination):
        #     if start==len(s):
        #         if left==0 and right==0 and open_count==0:
        #             result.append(" ".join(combination))
        #             return
        #     index=s[start]
        #     combination.append(index)
        #     if index=="(":
        #         backtrack(start+1,left,right,open_count+1,combination)
        #     elif index==")":
        #         if open_count>0:
        #             backtrack(start+1,left,right,open_count-1,combination)
        #     else:
        #         backtrack(start+1,left,right,open_count,combination)
                
        #     combination.pop()
            
        # backtrack(0,left,right,0,[])
        # return result
            
        
        # total_of_open=0
        # total_of_close=0
        # for i in range(len(s)):
        #     if s[i]=="(":
        #         total_of_open+=1
        #     if s[i]==")":
        #         total_of_close+=1
        # remain=abs(total_of_close-total_of_open)
        # bigger=max(total_of_open,total_of_close)
        # print(remain)
        # def backtrack(open,close,combination,start):
        #     if start==len(s):
        #         result.append(" ".join(combination))
        #         return
        #     if remain>0:
        #         total_parenthesis=bigger-remain
        #         # return total_parenthesis
        #     for i in range(start,len())
                        
s="(a)())()"
print(removeInvalidParentheses(s))