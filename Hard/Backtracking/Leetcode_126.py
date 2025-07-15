# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

def findLadders(beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set=set(wordList)
        if endWord not in word_set:
            return []
        
        patterns={}
        all_words = list(word_set)
        if beginWord not in word_set:
            all_words.append(beginWord)
        for word in all_words:
            for i in range(len(word)):
                pattern=word[:i]+'*'+word[i+1:]
                patterns.setdefault(pattern,[]).append(word)
        
        front,back={beginWord},{endWord}
        found=False
        # alphabet="abcdefghijklmnopqrstuvwxyz"
        neighbors={}
        flip=False
        while front and back and not found:
            if len(front)>len(back):
                front,back=back,front
                flip= not flip
            next_front=set()
            for word in front:
                # if word in word_set:
                #     word_set.remove(word)
                word_set.discard(word)
            for word in front:
                for i in range(len(word)):
                    pattern=word[:i]+'*'+word[i+1:]
                    for candidate in patterns.get(pattern, []):
                        if candidate not in word_set and candidate not in back:
                            continue
                        # candidate=word[:i]+character+word[i+1:]
                        # if candidate in word_set:
                        #     next_front.add(candidate)
                        if flip:
                                key,value=candidate,word
                                
                        else:
                                key,value=word,candidate
                        neighbors.setdefault(key,[]).append(value)
                        if candidate in back:
                                found=True
                        if candidate in word_set:
                            next_front.add(candidate)
                    
            front=next_front
        if not found:
            return []
        neighbors.setdefault(endWord, [])
        result=[]
        path=[beginWord]
        def backtrack(word):
            if word==endWord:
                result.append(path[:])
                return
            for nxt in neighbors.get(word,[]):
                path.append(nxt)
                backtrack(nxt)
                path.pop()
        backtrack(beginWord)
        return result                                               
        
        
        
                  
beginWord = "aaaaa"
endWord = "ggggg"
wordList = ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"]

print(findLadders(beginWord,endWord,wordList))


# word_set=set(wordList)
        # if endWord not in word_set:
        #     return []
        
        # distance={beginWord:0}
        # neighbor={beginWord:[]}
        # current_level=[beginWord]
        # alphabet="abcdefghijklmnopqrstuvwxyz"
        # found=False
        # while current_level and not found:
        #     next_level=[]
        #     for i in current_level:
        #         if i in word_set:
        #             word_set.remove(i)
        #     for word in current_level:
        #         if word not in neighbor:
        #             neighbor[word]=[]
        #         for i in range(len(word)):
        #             for character in alphabet:
        #                 if character==word[i]:
        #                     continue
        #                 candidate=word[:i]+character+word[i+1:]
        #                 if candidate in word_set:
        #                     neighbor[word].append(candidate)
        #                     if candidate not in distance:
        #                         distance[candidate]=distance[word]+1
        #                         if candidate==endWord:
        #                             found=True
        #                         else:
        #                             next_level.append(candidate)
        #     current_level=next_level 
        # if endWord not in distance:
        #     return []
        # if endWord not in neighbor:
        #     neighbor[endWord]=[]
        
        # result=[]
        # list=[beginWord]
        # def backtrack(word):
        #     if word==endWord:
        #         result.append(list[:])
        #         return
        #     for next_word in neighbor.get(word,[]):
        #         if distance.get(next_word,float('inf'))==distance[word]+1:
        #             list.append(next_word)
        #             backtrack(next_word)
        #             list.pop()
        # backtrack(beginWord)
        # return result