"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldToNew = {}

        # We don't have the copied pointers yet, so we'll iterate through and create nodes
        # with their values.
        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next

        # On the second pass, the nodes have been created so now we can wire up the pointers.
        cur = head
        while cur:
            newCur = oldToNew.get(cur)
            newCur.next = oldToNew.get(cur.next)
            newCur.random = oldToNew.get(cur.random)
            cur = cur.next
            
        return oldToNew[head]