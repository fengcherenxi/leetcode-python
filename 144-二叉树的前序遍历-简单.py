# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 前序遍历：
# 先输出当前节点
# 若左子节点不为空，则递归继续前序遍历
# 若右子节点不为空，则递归继续前序遍历
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root):
            if not root:
                return 
            res.append(root.val)
            if root.left!=None:
                preorder(root.left)
            if root.right!=None:
                preorder(root.right)
        res = []
        preorder(root)
        return res
