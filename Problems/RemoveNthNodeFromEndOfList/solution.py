# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        cur = head
        while cur:
            length += 1
            cur = cur.next

        removeNodeNo = length - n

        prev = None
        i = 0
        newHead = head
        while head:
            if i == removeNodeNo:
                if prev:
                    prev.next = head.next
                    head = prev
                else:
                    # We're removing the first node
                    head = head.next
                    newHead = head
            # If we've removed the lone node from a list that contained a single element,
            #   head could be null.
            if head:
                prev = head
                head = head.next
                i += 1

        return newHead
