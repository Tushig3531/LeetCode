# You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

# A 0-indexed string num of length n + 1 is created using the following conditions:

# num consists of the digits '1' to '9', where each digit is used at most once.
# If pattern[i] == 'I', then num[i] < num[i + 1].
# If pattern[i] == 'D', then num[i] > num[i + 1].
# Return the lexicographically smallest possible string num that meets the conditions.

 

# Example 1:

# Input: pattern = "IIIDIDDD"
# Output: "123549876"
# Explanation:
# At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
# At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
# Some possible values of num are "245639871", "135749862", and "123849765".
# It can be proven that "123549876" is the smallest possible num that meets the conditions.
# Note that "123414321" is not possible because the digit '1' is used more than once.
# Example 2:

# Input: pattern = "DDD"
# Output: "4321"
# Explanation:
# Some possible values of num are "9876", "7321", and "8742".
# It can be proven that "4321" is the smallest possible num that meets the conditions.

def smallestNumber(pattern):
        """
        :type pattern: str
        :rtype: str
        """
        stack=[] #initializing the stack 
        result=[] #initializing the result
        
        for i in range(1,len(pattern)+2): #loop the index between 1 to the end of the length of patter plus 2. Because if I use len(pattern) it would be n-1, so I need to use n+1.
            stack.append(i) #then add the i'th index to the stack basically "1,2,3,4,5,6,7,8,9"
            if i == len(pattern)+1 or pattern[i-1]=='I': #if the index is in the end or if the last index was equal to "I"
                while stack: #and that element is in the stack
                    result.append(str(stack.pop())) #pop that element out of the stack end append it into the stack. We are popping numbers from the stack because the stack holds numbers in reverse order when we encounter a 'D'. Popping them gives us the correct order 
        
        return ''.join(result) #put them in the string


        
pattern="IIIDIDDD"
print(smallestNumber(pattern))