# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solutions/2428167/easy-0-ms-100-fully-explained-java-c-python-js-c-python3/
    '''
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
    
        # Create nodes for nums left of mid
        root.left = self.sortedArrayToBST(nums[:mid])

        # Create nodes for nums right of mid
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root