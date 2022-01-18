# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 后序遍历
# 若左子节点不为空，则递归继续前序遍历
# 若右子节点不为空，则递归继续前序遍历
# 先输出当前节点
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if not root:
                return 
            if root.left:
                inorder(root.left)
            if root.right:
                inorder(root.right)
            res.append(root.val)
        res = []
        inorder(root)
        return res
