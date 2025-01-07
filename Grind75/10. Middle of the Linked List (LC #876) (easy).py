from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """ Two Pointers """

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow

        """ Initial Approach """

        # current = head
        # index = 0
        # visited = {}

        # while current:
        #     visited[index] = current
        #     current = current.next
        #     index += 1
        
        # return visited[index // 2]