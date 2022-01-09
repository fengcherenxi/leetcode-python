class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        Max = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d and d[s[i]]>start:
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]] = i
                Max = max(Max,i - start)
        return Max
