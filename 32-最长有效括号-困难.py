class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stc = [-1]
        res = 0
        for i,c in enumerate(s):
            if c=='(':
                stc.append(i)
            elif len(stc)==1:# 右括号且栈长为1，则移动栈底的数值
                stc.pop()
                stc.append(i)
            else:
                stc.pop()
                res=max(res,i-stc[-1])# 当前下标减去栈顶的值
        return res
