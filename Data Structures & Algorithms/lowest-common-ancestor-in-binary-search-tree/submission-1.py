# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If I trace the path from the root to that node given that it is a BST, I can get a list denoting this path. Then I want to find the element in both lists that occurs the latest.
        # The ancestor prefixes will be the same until they're not.
        # Consider 1 and 4 in Example 1: [5,3,1] and [5,3,4]. We keep going in both until one list ends or until lineageP[i] != lineageQ[i]. At which point, we return lineageP[i-1].
        lineage = defaultdict(list)

        def genealogy(root: TreeNode, node: TreeNode):
            lineage[node.val].append(root)
            if root.val > node.val:
                genealogy(root.left, node)
            elif root.val < node.val:
                genealogy(root.right, node)

        genealogy(root, p)
        genealogy(root, q)

        lineageP = lineage[p.val]
        lineageQ = lineage[q.val]

        i = 0
        while i < len(lineageP) and i < len(lineageQ) and lineageP[i].val == lineageQ[i].val:
            i += 1

        return lineageP[i-1]

