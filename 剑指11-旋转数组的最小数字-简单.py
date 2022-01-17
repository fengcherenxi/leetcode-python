# 二分查找注意越界问题
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers)-1
        while left<right:
            mid = (left+right)//2
            if numbers[mid]<numbers[right]:
                right = mid
            elif numbers[mid]>numbers[right]:
                left = mid+1
            else:
                right-=1
        return numbers[right]

'''
# 遍历查找
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        for i in range(len(numbers))[::-1]:
            if i==0:
                return numbers[0]
            if numbers[i]<numbers[i-1]:return numbers[i]
            else:
                continue
'''
