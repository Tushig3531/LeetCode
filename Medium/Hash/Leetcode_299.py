# You are playing the Bulls and Cows game with your friend.
# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
# Example 1:
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
 
 
def getHint(secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls=0
        cows=0
        
        hashmap_sec={}
        for ch in secret:
            hashmap_sec[ch]=hashmap_sec.get(ch,0)+1
        # hashmap_g={}
        # for num_g in guess:
        #     hashmap_g[num_g]=hashmap_g.get(num_g,0)+1
        # return hashmap_sec, hashmap_g
        # for num, count in hashmap_sec.items():
                # return count
        for i, ch in enumerate(guess):
            if ch==secret[i]:
                bulls+=1
                hashmap_sec[ch]-=1
        for i,ch in enumerate(guess):
            if ch!=secret[i] and hashmap_sec.get(ch,0)>0:
                cows+=1
                hashmap_sec[ch]-=1
        return str(bulls)+"A"+str(cows)+"B"
        
                
        
        
secret = "1807"
guess = "7810"
print(getHint(secret,guess))