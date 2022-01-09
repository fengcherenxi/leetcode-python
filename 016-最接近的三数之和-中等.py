class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = nums[0] + nums[1] + nums[len(nums)-1]

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if abs(val-target)<abs(ans-target):
                    ans = val
                elif val<target:l+=1
                else:r-=1
        return ans
