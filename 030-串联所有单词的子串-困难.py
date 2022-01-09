class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        a = len(words[0])
        slen = a*len(words)
        res = []
        for i in range(len(s)-slen+1):
            s0 = s[i:i+slen]
            #print(s0)
            b_words = words[:]
            j=0
            while j < slen-a+1:
                #print(s0[j:j+a])
                if s0[j:j+a] in b_words:
                    b_words.remove(s0[j:j+a])
                    #print(b_words)
                    if len(b_words)==0:
                        res.append(i)
                    j+=a
                else:
                    break
        return res
