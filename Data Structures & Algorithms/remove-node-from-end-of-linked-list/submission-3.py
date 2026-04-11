# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        p =head
        for _ in range(n):
            p = p.next
        
        q , prev = head, None
        while p :
            p = p.next
            prev =q
            q = q.next
        
        if q==head:
            return head.next
        prev.next = q.next
        q.next = None

        return head


        