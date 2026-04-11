# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      
        if not list1:
            return list2
        if not list2:
            return list1

        q = list1
        p = list2
        
        newHead = ListNode()
        curr = newHead

        while p and q:
          
            if p.val <= q.val:
                temp = p.next 
                p.next = None
                curr.next = p
                p = temp
            else: 
                temp = q.next 
                q.next = None
                curr.next = q
                q = temp
            curr = curr.next

        if not p: 
                curr.next = q
        if not q: 
            curr.next = p
        
        return newHead.next
        


        


        