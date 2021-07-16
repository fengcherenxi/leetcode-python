#借用python中集合的特点：set(list)得到的集合不含重复元素且进行了排序。如set([1,3,2,1])={1,2,3} 因此直接判断set后的集合与原来的list的长度是否相等即可求解。
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)         
        if len(nums)==len(a):             
            return False         
        else:             
            return True