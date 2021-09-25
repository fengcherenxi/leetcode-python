class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        b=len(num)
        if b%2==0:
            a=(num[int(b/2)-1]+num[int(b/2)])/2
        else:
            a=num[int(b/2)]
        return a
# 合并+sort最为简单