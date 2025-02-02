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

class Solution(object):
    def letterCombinations(self, digits):
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
        combination=[""] #it should start with empty

        for digit in digits: #2,3
            letters=keys[digit] #Letters in 2 and 3
            new_combination=[] #making new combination
            for base in combination: #making the base: ""
                for letter in letters: #a,b,c,d,e,f
                    new_combination.append(base+letter) #"ad","ae","af","bd","be","bf","cd","ce","cf"
            combination=new_combination
        return combination

