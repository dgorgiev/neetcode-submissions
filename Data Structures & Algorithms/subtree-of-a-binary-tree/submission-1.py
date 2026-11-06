# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # node root == node subroot
        # root left is sub tree of subroot left // and same for right
        def rec(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            # if root val  not equal subroot val then False
            if not subRoot and not root:
                return True
            elif subRoot and root and subRoot.val == root.val:
                return rec(root.left, subRoot.left) and rec(root.right, subRoot.right)
            return False
        
        def check(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not root and not subRoot:
                return True
            elif not root:
                return False
            elif not subRoot:
                return True
            if root.val == subRoot.val:
                return rec(root, subRoot) or check(root.left, subRoot) or check(root.right, subRoot)
            else:
                return check(root.left, subRoot) or check(root.right, subRoot)
        return check(root, subRoot)
            