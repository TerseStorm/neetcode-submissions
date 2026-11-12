# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # go to the smallest element and do an in-order traversal
        res = -1
        count = 0
        def inOrderTraversal(root, count, k, res):
            if root is not None:
                count, res = inOrderTraversal(root.left, count, k, res)
                count += 1
                if res != -1:
                    return count, res
                if count == k:
                    return count, root.val
                count, res = inOrderTraversal(root.right, count, k, res)
                if res != -1:
                    return count, res
            return count, res
        
        _, res = inOrderTraversal(root, count, k, res)
        return res