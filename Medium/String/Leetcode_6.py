# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result=[]
        logic=2*numRows-2
        if numRows==1:
            result=s
            return result
        for index in range(numRows):
            for position in range(index,len(s),logic):
                result.append(s[position])
                if index!=0 and index!=numRows-1 and position+logic-2*index<len(s):
                    result.append(s[position+logic-2*index])
        return "".join(result)
s="PAYPALISHIRING"
numRows=4
print(convert(s,numRows))

# n=4	4+2	6	2(n-1)							
# 1			7			13			19	
# 		4,2								
# 2		6	8		12	14		18		
# 		2,4								
# 3	5		9	11		15	17			
# 		6								
# 4			10			16				
										
# n=3	3+1	4	2(n-1)							
# 1		5		9		13		17		
# 		2,2								
# 2	4	6	8	10	12	14	16	18		
# 		4								
# 3		7		11		15		19		
										
															
# n=2	2	2(n-1)								
# 1	3	5	7	9	11	13	15			
# 2	4	6	8	10	12	14	16			
										
# n=1										
# 1	2	3	4	5	6	7	8			
										
										
# n=5	8	2(n-1)								
# 1				9				17		
# 	6,2									
# 2			8	10			16	18		
# 	4,4									
# 3		7		11		15		19		
# 	2,6									
# 4	6			12	14			20		
# 	8									
# 5				13				21		
										
# n=6	10	2(n-1)								
# 1					11					21
# 	8-2									
# 2				10	12				20	22
# 	6-4									
# 3			9		13			19		23
# 	4-6									
# 4		8			14		18			24
# 	2-8									
# 5	7				15	17				25
# 	10									
# 6					16					26