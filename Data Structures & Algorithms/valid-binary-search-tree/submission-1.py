# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isInBound(val, mini, maxi) -> bool:
            b1 = mini is None or val > mini
            b2 = maxi is None or val < maxi
            return b1 and b2

        def rec(node: TreeNode, mini: Optional[int], maxi:Optional[int]) -> bool:
            if not node:
                return True
            if not isInBound(node.val, mini, maxi):
                return False

            return rec(node.left, mini, node.val) and rec(node.right, node.val, maxi)

        return rec(root, None, None)

