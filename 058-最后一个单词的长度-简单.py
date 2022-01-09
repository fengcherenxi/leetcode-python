class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = []
        for i in range(len(s))[::-1]:
            if s[i] !=' ':
                res.append(i)
            elif len(res)==0:
                continue
            else:
                break
        return len(res)
