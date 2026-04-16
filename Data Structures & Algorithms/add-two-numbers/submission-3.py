# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        p = l1
        q = l2
        reminder =0 
        newHead = ListNode(0)
        newPointer = newHead
        
        while p and q:
            sumDigit = p.val + q.val + reminder
            digit = sumDigit%10
            reminder =sumDigit//10

            newNode = ListNode(digit)
            newPointer.next = newNode
            newPointer = newPointer.next
            p=p.next
            q=q.next
        
        if not q and not p:
            if reminder!=0:
                newNode = ListNode(reminder)
                newPointer.next = newNode
            return newHead.next
        elif not q:
            ls = p
        else:
            ls = q

        while ls:
            sumDigit = ls.val + reminder
            digit = sumDigit%10
            reminder =sumDigit//10
            
            newNode = ListNode(digit)
            newPointer.next = newNode
            newPointer = newPointer.next
            ls=ls.next
        
        if reminder!=0:
            newNode = ListNode(reminder)
            newPointer.next = newNode
   
        
        return newHead.next














        