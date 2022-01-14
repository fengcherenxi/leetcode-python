# 1:遍历+查找
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        arr = set()# 哈希集合比列表效率高
        for i in nums:
            if i in arr:
                return i
            else:
                arr.add(i)
