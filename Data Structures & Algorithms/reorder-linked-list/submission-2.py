# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #part the list to 2 halfs 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
     
        print(f'middle is {slow.val}')

        #revers the second half
        curr= slow.next
        prev = slow.next = None #have to discinnect other wise infinet loop is created
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        
        secondHalf = prev
        firstHalf = head

        while firstHalf and secondHalf:
            temp1 = firstHalf.next
            firstHalf.next = secondHalf
            firstHalf = temp1
            temp2 = secondHalf.next
            secondHalf.next = firstHalf
            secondHalf = temp2

            




        