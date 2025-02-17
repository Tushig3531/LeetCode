# An additive number is a string whose digits can form an additive sequence.
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
# Given a string containing only digits, return true if it is an additive number or false otherwise.
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
# Example 1:
# Input: "112358"
# Output: true
# Explanation: 
# The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# Example 2:
# Input: "199100199"
# Output: true
# Explanation: 
# The additive sequence is: 1, 99, 100, 199. 
# 1 + 99 = 100, 99 + 100 = 199

def isAdditiveNumber(num):
        """
        :type num: str
        :rtype: bool
        """
        def backtrack(remain, start,sequence):
            if start==len(num):
                return len(sequence)>=3
            for i in range(start+1,len(num)+1):
                number_in_string=num[start:i]
                if len(number_in_string)>1 and number_in_string[0]=="0":
                    continue
                number_in_int=int(number_in_string)
                
                if len(sequence)>=2 and number_in_int!=sequence[-1]+sequence[-2]:
                    continue
                sequence.append(number_in_int)
                if backtrack(remain,i,sequence):
                    return True
                sequence.pop()
            return False
        return backtrack(num,0,[])
            
            
            
                
        
        
        
num="112358"
print(isAdditiveNumber(num))