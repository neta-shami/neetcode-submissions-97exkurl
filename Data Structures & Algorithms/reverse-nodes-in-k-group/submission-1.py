# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head.next:
            return head

        newHead = ListNode()
        newListP = newHead
        
        count = 0
        startGroup , endGroup , nextGroup = head , head , head
        
        while nextGroup:
            while nextGroup and count<k:
                endGroup = nextGroup
                nextGroup = nextGroup.next 
                count+=1
            
            if count<k: #less then k remain
                newListP.next = startGroup
                return newHead.next
            
            endGroup.next = None
            prev = None
            count = 0

            while startGroup:
                temp = startGroup.next
                startGroup.next = prev
                prev =startGroup
                startGroup= temp
            
            newListP.next = prev
            while newListP.next: #keep new list pointer at the end of the new list
                newListP = newListP.next
            
            startGroup = nextGroup
        
        return newHead.next


        