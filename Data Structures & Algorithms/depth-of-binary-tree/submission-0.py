# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def rec(node: TreeNode, currDepth: int):
            if not node:
                return currDepth - 1
            return max(rec(node.left, currDepth + 1), rec(node.right, currDepth + 1))
        return rec(root, 1)