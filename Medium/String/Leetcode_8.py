# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

def myAtoi(s):
    result = []    
    index=0
    result=0
    operation=1
    lower_bound= -2**31
    upper_bound= 2**31-1
    
    s=s.strip() #This elimimates the blank spaces infront of the digit
    if not s:
        return 0 #If there is nothing return 0
    if s[index]=="+":
        operation=1 
        index=index+1
    elif s[index]=="-":
        operation= -1
        index=index+1
    
    while index<len(s) and s[index].isdigit():
        digit=int(s[index])
        if result>(upper_bound-digit)//10:
            if operation == 1:
                return upper_bound 
            else:
                return lower_bound
        result=result*10+digit
        index+=1   
   
    return result*operation

print(myAtoi("     3213123-sqofjqwf-3132"))
