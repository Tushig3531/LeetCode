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
                return len(sequence)>=3 #must have at least 3 numbers
            for i in range(start+1,len(num)+1): #If I start from 0 it will be empty so starting from the next index to the end
                number_in_string=num[start:i] #turning them into string, and extracting them, "1", "11", "112"...
                if len(number_in_string)>1 and number_in_string[0]=="0": #if the length of the string is bigger than 1 which is true, but if the first index is zero
                    continue #it shouldn't take that value
                number_in_int=int(number_in_string) #convert them into the integer
                
                if len(sequence)>=2 and number_in_int!=sequence[-1]+sequence[-2]: #if the length of the sequence basically the length of the combination is bigger than 2, which is just test statement. But the sum of the last two combination of sequences is not the equal to the number. 
                    continue #it should ignore too
                sequence.append(number_in_int) #then put them in the sequence
                if backtrack(remain,i,sequence): #Recursively calls the function but at the next time, the starting index will be i
                    return True #if it is follwing all those conditions return True
                sequence.pop() #and pop the unnecessary, overflow sequences
            return False #else return false
        return backtrack(num,0,[]) #init
num="112358"
print(isAdditiveNumber(num))