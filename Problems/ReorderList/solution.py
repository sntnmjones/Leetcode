# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find middle. If odd length, fast will be longer
        # e.g. [1,2,3,4,5] -> [1,2], [3,4,5]
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Create two halves
        head2 = slow.next
        slow.next = None

        # Reverse second half
        prev = None
        while head2:
            tmp = head2.next
            head2.next = prev
            prev = head2
            head2 = tmp

        # merge two halfs
        # Example Initially [1,2,4,3]
        first, second = head, prev  # 1, 4
        while second:
            tmp1, tmp2 = first.next, second.next    # iter1: 2, 3; iter2: None, None
            first.next = second # iter1: 4; iter2: 3
            second.next = tmp1  # iter1: 2; iter2: None
            first, second = tmp1, tmp2  # iter1: 2, 3; iter2: None, None
            