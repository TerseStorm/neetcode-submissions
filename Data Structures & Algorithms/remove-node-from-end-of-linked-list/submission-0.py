# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        res = ListNode(33)
        res.next = head

        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next

        """
        THINKING:
            - 1 is the end of the list.
            - 2 is the penultimate value.
            - ... 
            - length is the first value.
        """

        if n == length:
            return head.next
        
        target = length - n
        cur = head
        prev = None
        i = 0
        while i < target:
            prev = cur
            cur = cur.next
            i += 1

        prev.next = cur.next
        return res.next

