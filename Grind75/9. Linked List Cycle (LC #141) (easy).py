from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        """ Two pointers """

        fast = head
        slow = head

        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        
        return False

        """ Initial approach """

        # current = head
        # visited = set()

        # while current is not None:
        #     if current in visited:
        #         return True
        #     visited.add(current)
        #     current = current.next
        
        # return False