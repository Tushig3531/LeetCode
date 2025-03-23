# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 
# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

def minDistance(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        number_of_rows=len(word1)+1
        number_of_columns=len(word2)+1
        matrix=[]
        matrix = [[float("inf") for _ in range(number_of_columns)] for _ in range(number_of_rows)]
        
        for j in range(number_of_columns):
            matrix[len(word1)][j]=len(word2)-j
        for i in range(number_of_rows):
            matrix[i][len(word2)]=len(word1)-i
            
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    matrix[i][j]=matrix[i+1][j+1]
                else:
                    matrix[i][j]=1+min(matrix[i+1][j],matrix[i][j+1],matrix[i+1][j+1])
        return matrix[0][0]
        
        
        
        
        
word1 = "horse"
word2 = "ros"

print(minDistance(word1, word2))
        