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
        """
            THINKING:
                - We have to make a constant number of passes through the list, at least 1. (O(n) time)
                - We can only store a constant amount of data. (O(1) space)
                - pass through list to find its length.
                - midpoint index is length // 2 for an odd-sized list.
                - midpoint index is length / 2 - 1 for an even-sized list.
                - reverse the second half of the list so that it points from the end to the midpoint.
                - keep hold of the end of the list.
                - start = head and end = end of list node
                - while end is not None and start is not None or pos(start) == pos(end):
                    - tempStartNext = start.next
                    - tempEndNext = end.next
                    - start.next = end
                    - start.next.next = tempStartNext
                    - start = start.next.next
                    - end = tempEndNext

                - Something like this, but remember the visualiser.
       
       """
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

      


    
    
    