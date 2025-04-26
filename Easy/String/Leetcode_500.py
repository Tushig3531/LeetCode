# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
# Example 1:
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Explanation:
# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.
# Example 2:
# Input: words = ["omk"]
# Output: []
# Example 3:
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]

def findWords(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row=set("qwertyuiop")
        second_row=set("asdfghjkl")
        third_row=set("zxcvbnm")
        def hashing(x):
            hashmap={}
            for ch in x:
                hashmap[ch]=hashmap.get(ch,0)+1
            return hashmap
        valid=[]
        for word in words:
            lower_word=word.lower()
            count=hashing(lower_word)
            letter=set(count.keys())
            if letter<=first_row or letter<=second_row or letter<=third_row:
                valid.append(word)
        return valid
            
        
        
words = ["Hello","Alaska","Dad","Peace"]     
print(findWords(words))