# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        if head.next is None:
            return None    
        res = ListNode(33)
        res.next = head

        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next

        if length % 2 == 0:
            midpoint = (length / 2) - 1
        else:
            midpoint = length // 2

        count = 0
        cur = head
        while count < midpoint:
            cur = cur.next
            count += 1
        # current node is the midpoint node
        secondHalf = cur.next
        cur.next = None

        # reverse secondHalf
        curr, prev = secondHalf, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp


        # first half of list (start -> midpoint)
        start = head

        # second half of list (end -> midpoint + 1)
        end = prev

        while end is not None:
            startNextTemp = start.next
            start.next = end
            start = start.next
            end = startNextTemp