# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
# Example 1:
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:
# Input: tiles = "AAABBC"
# Output: 188
# Example 3:
# Input: tiles = "V"
# Output: 1

def numTilePossibilities(tiles):
        """
        :type tiles: str
        :rtype: int
        """
        result=[]
        tiles=sorted(tiles) #sorting it to try not to confuse myself
        def backtrack(used,combination): #I am using used and combination parameters
            if combination: #if combination have every combination
                result.append(list(combination)) #append it to the list of result
            for i in range(len(tiles)): #loop in length of tiles
                if used[i]: #if used[i] is True, basically if it is used
                    continue #ignore
                if i>0 and tiles[i]==tiles[i-1] and not used[i-1]:#if i is greater 0, tiles' i-th index is equal to i-1 and i-1 is used. Ignore
                    continue
                used[i]=True 
                combination.append(tiles[i]) #append it into the combination
                backtrack(used,combination) #recursively call the function
                combination.pop()# pop the overflow
                used[i]=False #turn it to false
        backtrack(([False]*len(tiles)),[]) #Turning every value into False. For example "AAB"-->"False, False, False"
        return len(result)
        
        
tiles="AAB"
print(numTilePossibilities(tiles))