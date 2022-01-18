# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 广度优先算法+队列实现，注意输出hi列表形式，里面对应的是节点值不是节点，因此要多设置一个空数组用来记录节点值
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        ans = []
        res = []
        deque_list = [root]
        while deque_list:
            for i in range(len(deque_list)):
                node = deque_list.pop()
                if node:
                    res.append(node.val)
                if node.left:
                    deque_list.insert(0,node.left)
                if node.right:
                    deque_list.insert(0,node.right)
            ans.append(res)
            res = []
        return ans
