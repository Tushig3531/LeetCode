# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"

def multiply(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0" in [num1,num2]:
            return "0"
        result=[0]*(len(num1)+len(num2))
        num1,num2=num1[::-1],num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit=int(num1[i1])*int(num2[i2])
                result[i1+i2]+=(digit)
                result[i1+i2+1]+=(result[i1+i2]//10)
                result[i1+i2]=result[i1+i2]%10
        result,begin=result[::-1],0
        while begin<len(result) and result[begin]==0:
            begin+=1
        result=map(str,result[begin:])
        return "".join(result)
        
num1 = "123"
num2 = "456"

print(multiply(num1,num2))