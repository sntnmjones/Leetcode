# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()

        if root:
            q.append(root)

        res = []
        while q:
            levelSize = len(q)
            levelNodes = []

            for _ in range(levelSize):
                curNode = q.popleft()

                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)

                levelNodes.append(curNode.val)
            
            res.append(levelNodes)

        return res