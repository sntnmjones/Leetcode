# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True

        isSubtreeInLeft = self.isSubtree(root.left, subRoot)
        isSubtreeInRight = self.isSubtree(root.right, subRoot)

        return isSubtreeInLeft or isSubtreeInRight

            
    def isSameTree(self, a, b):
        if not a and not b:
            return True
        if a and b and a.val == b.val:
            isLeftSame = self.isSameTree(a.left, b.left)
            isRightSame = self.isSameTree(a.right, b.right)
            return isLeftSame and isRightSame 
        return False