# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_list = []
        num2_list = []

        # Put numbers into stack
        while l1:
            num1_list.append(l1.val)
            l1 = l1.next

        while l2:
            num2_list.append(l2.val)
            l2 = l2.next

        # Reverse numbers
        num1_list = num1_list[::-1]
        num2_list = num2_list[::-1]

        # Create numbers
        num1_str = ''.join(map(str, num1_list))
        num2_str = ''.join(map(str, num2_list))
        num1 = int(num1_str)
        num2 = int(num2_str)

        # Add numbers
        num3 = num1 + num2

        # Parse result to list
        num3_list = []
        for digit_str in str(num3):
            num3_list.append(int(digit_str))
        
        # Reverse result
        num3_list = num3_list[::-1]

        # Create linked list
        result = ListNode()
        cur = result
        for num in num3_list:
            cur.next = ListNode(num)
            cur = cur.next

        return result.next