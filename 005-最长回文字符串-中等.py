class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 两种判断条件，奇数情况和偶数情况
        # 动态规划
        # 先遍历字母，再以字母为中心向两边扩展
        pre = ''
        for i in range(len(s)):
            len1 = len(self.getlongestPalindrome(s,i,i))
            if len1>len(pre):
                pre = self.getlongestPalindrome(s,i,i)
            len2 = len(self.getlongestPalindrome(s,i,i+1))
            if len2>len(pre):
                pre = self.getlongestPalindrome(s,i,i+1)
        return pre
    
    def getlongestPalindrome(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
