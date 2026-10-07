# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.newHead = None
        self.curPointer = None
        # Special Cases, Akin?
        #   - both lists are empty
        if list1 is None and list2 is None:
            return None
        #   - one list is empty
        while list1 is not None and list2 is None:
            self.addToNewList(list1.val)
            list1 = list1.next
        while list1 is None and list2 is not None:
            self.addToNewList(list2.val)
            list2 = list2.next
        while list1 is not None or list2 is not None:
            if (list1 is not None and list2 is None) or (list1 is not None and list2 is not None and list1.val <= list2.val):
                self.addToNewList(list1.val)
                list1 = list1.next
            elif  (list1 is None and list2 is not None) or (list1 is not None and list2 is not None and list1.val > list2.val):
                self.addToNewList(list2.val)
                list2 = list2.next
        return self.newHead

    def addToNewList(self, val):
        node = ListNode(val)
        if self.newHead is None:
            self.newHead = node
            self.curPointer = node
        else:
            self.curPointer.next = node
            self.curPointer = node
            