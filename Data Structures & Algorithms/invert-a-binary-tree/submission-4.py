# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative version of the recursive solution. Uses an explicit stack over an implicit one.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        stack = [root]
        while stack:
            cur = stack.pop(0)
            if cur.left:
                stack.insert(0, cur.left)
            if cur.right:
                stack.insert(0, cur.right)
            cur.left, cur.right = cur.right, cur.left
        return root

        