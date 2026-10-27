# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def invert_d1(root: TreeNode):
            root.left, root.right = root.right, root.left
            if root.left:
                invert_d1(root.left)
            if root.right:
                invert_d1(root.right)
            return
        invert_d1(root)
        return root



        