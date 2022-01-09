class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 重点：先按照start排序
        if len(intervals)==1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        result = []
        i = 0 
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0] and intervals[i][0]<=intervals[i+1][1]:
                intervals[i+1]=[min(intervals[i][0],intervals[i+1][0]),max(intervals[i][1],intervals[i+1][1])]
            else:
                result.append(intervals[i])
            i+=1
        result.append(intervals[-1])
        return result
'''
此方法是最简单的方法
主要浪费时间和空间的地方是排序过程
时间复杂度：O(n\log n)O(nlogn)，其中 nn 为区间的数量。除去排序的开销，我们只需要一次线性扫描，所以主要的时间开销是排序的 O(n\log n)O(nlogn)。
空间复杂度：O(\log n)O(logn)，其中 nn 为区间的数量。这里计算的是存储答案之外，使用的额外空间。O(\log n)O(logn) 即为排序所需要的空间复杂度。
'''
