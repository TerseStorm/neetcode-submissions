# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = defaultdict(list)

        def bfs(root, level):
            if root is not None:
                levels[level].append(root.val)
                bfs(root.left, level + 1)
                bfs(root.right, level + 1)

        bfs(root, 0)

        res = []
        for i in range(len(levels.keys())):
            res.append(levels[i])
        return [item[-1] for item in res]