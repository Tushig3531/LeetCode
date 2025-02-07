# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]


def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        keys={
            "2":"abc","3":"def",
            "4":"ghi","5":"jkl","6":"mno",
            "7":"pqrs","8":"tuv","9":"wxyz"
        }
        result=[]
        def backtrack(utga,husnegt):
            if utga==len(digits): #if the length of digits are equal to index
                result.append("".join(husnegt)) #we gonna append the path in to the result
                return
            possible_letters=keys[digits[utga]] #possible_letters are the keys of digits' index
            for letter in possible_letters: #looping those possible_letters
                husnegt.append(letter) #inserting those letters in path
                backtrack(utga+1,husnegt) #Then moves to the next index
                husnegt.pop()
        backtrack(0,[]) #initial 
        return result
digits="23"
print(letterCombinations(digits))        

