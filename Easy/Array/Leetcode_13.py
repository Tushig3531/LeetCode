# # Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result=0
        for i in range(len(s)):
            if i<len(s)-1 and values[s[i]]<values[s[i+1]]:
                result=result-values[s[i]]
                
            else:
                result=result+values[s[i]]
        return result
    
romanTest="III"
Test=romanToInt(romanTest)
print(Test)

# Here I inserted the roman numbers as a varaibles and equalized result with 0, then we can insert our value in result.
# Then I used for loop the "s". Thus our "s" will look like this 0) I 1) I 2) I. 
# Then I used if function. When the length of "s" minus 1 (basically it is preventing the index out of the range) and gives condition that if the value of s[i] is bigger less then s[i+1]. Which means the value of first index is less then the next index. For example: IX, I is less than X.
# If the "s" under those circumstances, it will minus value of the index. For example: "IX" I is less then X, so we minus I from X which is equal to 9.
# Else, plus: For example: XI, X is bigger than I. So we add I on X which is equal to 11.



