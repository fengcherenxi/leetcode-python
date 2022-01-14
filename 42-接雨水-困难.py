'''
# 方法1：动态规划，三次遍历
class Solution:
    def trap(self, height: List[int]) -> int:
        left_arr = [height[0]]
        left_max = height[0]
        right_arr = [height[-1]]
        right_max = height[-1]
        res = 0
        for i in height[1:]:
            left_max = max(left_max,i)
            left_arr.append(left_max)
        for i in height[:len(height)-1][::-1]:
            right_max = max(right_max,i)
            right_arr.insert(0,right_max)
        for i in range(len(height)):
            res += min(left_arr[i],right_arr[i]) - height[i]
        return res
'''
'''
# 方法2：单调递减栈,时间更快一次遍历，但空间复杂度依然可以优化
class Solution:
    def trap(self, height: List[int]) -> int:
        stc = []
        res = 0
        n = len(height)
        for i,h in enumerate(height):
            while stc and h>height[stc[-1]]:
                top = stc.pop()
                if not stc:
                    break
                left = stc[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                res += currWidth * currHeight
            stc.append(i)
        return res
'''
# 方法3：双指针优化空间复杂度
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height)-1
        l_max,r_max = 0,0
        while l<r:
            l_max = max(l_max,height[l])
            r_max = max(r_max,height[r])
            if height[l]<height[r]:
                res+=l_max-height[l]
                l += 1
            else:
                res += r_max-height[r]
                r -= 1
        return res
