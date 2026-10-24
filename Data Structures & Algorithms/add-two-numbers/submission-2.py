# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def safeVal(lN):
            if lN is None:
                return 0
            return lN.val

        def safeNext(lN):
            if lN is None:
                return None
            return lN.next

        finalSum = ListNode()
        cur = finalSum
        carry = 0
        while l1 is not None or l2 is not None:
            s = safeVal(l1) + safeVal(l2) + carry
            sNode = ListNode(s % 10)
            cur.next = sNode
            cur = sNode
            carry = s // 10
            l1 = safeNext(l1)
            l2 = safeNext(l2)
        if carry > 0:
            cNode = ListNode(carry)
            cur.next = cNode
        return finalSum.next