# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 中序遍历+有序二叉树可以实现从小到大检索
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if not root:
                return 
            if root.left:
                inorder(root.left)
            res.append(root.val)
            if root.right:
                inorder(root.right)
        res = []
        inorder(root)
        return res
