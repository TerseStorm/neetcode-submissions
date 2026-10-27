# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# We cannot change the defnition of a List Node.
# Instead, we wrap it and "implement the Comparable interface"
# This Allows you to compare nodes and therefore let the minHeap get to work 
class ComparableNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, cNode):
        return self.node.val < cNode.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        finalList = ListNode()
        cur = finalList

        minHeap = []
        # add all nodes to minHeap
        for lst in lists:
            while lst is not None:
                heapq.heappush(minHeap, ComparableNode(lst))
                lst = lst.next

        
        # with all nodes in the minHeap, remove them to sort the list:

        while len(minHeap) > 0:
            minNode = heapq.heappop(minHeap)
            cur.next = minNode.node
            cur = cur.next
        return finalList.next