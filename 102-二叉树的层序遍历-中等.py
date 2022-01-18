# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 广度优先算法+队列实现，注意输出hi列表形式，里面对应的是节点值不是节点，因此要多设置一个空数组用来记录节点值
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        layer = [root]
        ans = []
        while layer:
            res = []
            for i in range(len(layer)):
                a = layer.pop()
                res.append(a.val)
                if a.left:
                    layer.insert(0,a.left)
                if a.right:
                    layer.insert(0,a.right)
            ans.append(res)
        return ans
