# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_s=[]
        if not s:
            return True
        for character in s:
            if ('a'<=character<='z') or ('A'<=character<='Z') or ('0'<=character<='9'):
                cleaned_s.append(character.lower())
        clean= ''.join(cleaned_s)
        return clean==clean[::-1]
        
        
        
s="A man, a plan, a canal: Panama"
print(isPalindrome(s))