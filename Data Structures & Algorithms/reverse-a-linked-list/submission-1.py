# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head is not None:
            # store reference to true next
            trueNext = head.next
            # make head point to prev
            head.next = prev
            if trueNext is not None:
                # make prev the current head
                prev = head
                # make the current head the true next
                head = trueNext
            else:
                return head
        return head