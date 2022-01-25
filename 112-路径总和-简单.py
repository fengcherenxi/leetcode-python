# 递归
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 广度优先【队列】
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:return False
        que_node = [root]
        que_val = [root.val]
        while que_node:
            now = que_node.pop()
            temp = que_val.pop()
            if not now.left and not now.right:
                if temp == targetSum:
                    return True 
            if now.left:
                que_node.insert(0,now.left)
                que_val.insert(0,now.left.val+temp)
            if now.right:
                que_node.insert(0,now.right)
                que_val.insert(0,now.right.val+temp)
        return False
'''
