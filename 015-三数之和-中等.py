class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue# 跳过后满部分进入下一次循环
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        while i<len(nums)-2:
            target = -nums[i]

            # 内部细节
            h={}
            j = i+1
            while j<len(nums):
                current = nums[j]
                if current in h:
                    a=[nums[i],h[current],nums[j]]
                    if a not in result:
                        result.append(a)
                else:
                    h[target-current] = current
                j = j+1
            i = self.skip_dup(i,nums)
        return result
    # 跳过重复值
    def skip_dup(self,i:int,nums:List[int]) -> int:
        n = i+1
        while n<len(nums) and nums[n]==nums[i]:
            n+=1
        return n
'''
