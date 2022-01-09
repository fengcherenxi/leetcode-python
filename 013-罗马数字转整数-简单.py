class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        ans = 0

        for i in range(len(s)):
            if i > 0 and dic[s[i]] > dic[s[i-1]]:
                ans += dic[s[i]] - 2*dic[s[i-1]]
            else:
                ans += dic[s[i]]
        return ans
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        ans = 0
        i = 0
        while i < len(s):
            if i<len(s)-1 and dic[s[i]] < dic[s[i+1]]:
                temp = dic[s[i+1]] - dic[s[i]]
                i += 2
            else:
                temp = dic[s[i]]
                i += 1
            print(temp)
            ans += temp
        return ans
'''
