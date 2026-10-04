# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative version of the recursive solution. Uses an explicit stack over an implicit one. BFS through binary tree.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        # push root to stack
        stack = [root]
        while stack:
            # remove current node from stack
            cur = stack.pop(0)
            # we will traverse its left child next.
            if cur.left:
                stack.insert(0, cur.left)
            # we will traverse the right child after.
            if cur.right:
                stack.insert(0, cur.right)
            # we swap them around on the root.
            cur.left, cur.right = cur.right, cur.left
        return root

        