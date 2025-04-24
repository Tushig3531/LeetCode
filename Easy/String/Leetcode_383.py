# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_hash={}
        magazine_hash={}
        for ch in ransomNote:
            ransom_hash[ch]=ransom_hash.get(ch,0)+1
        for ch in magazine:
            magazine_hash[ch]=magazine_hash.get(ch,0)+1
        # print(ransom_hash)
        # print(magazine_hash)
        for ch,required in ransom_hash.items():
            if magazine_hash.get(ch,0)<required:
                return False
        return True
        
            
        
        

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote,magazine))