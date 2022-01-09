class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]# 指定第一个字符串中的每一个字符为对比对象
            for j in range(1, count): # 向后遍历每一个字符串
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        prefix, count = strs[0], len(strs)
        for i in range(1,count):
            prefix = self.two_index(prefix,strs[i])
            if prefix=="":break
        return prefix
    def two_index(self,str1:str,str2:str) -> str:
        #if not str1 or not str2:return ""
        a = min(len(str1),len(str2))
        index = 0
        while index<a and str1[index]==str2[index]:
            index+=1
        return str1[:index]
'''
