"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        newHead = Node(0)
        q = newHead
        p = head
        table = defaultdict(Node)

        while p:
            newNode = Node(p.val)
            pointer = newNode
            table[p] = pointer
            q.next = newNode
            q = q.next
            p = p.next
        
        q = newHead.next
        p = head

        while q:
            if p.random == None:
                q.random = None
            else:
                randomP = p.random
                randomQ = table[randomP]
                q.random = randomQ

            p = p.next
            q = q.next
        
        return newHead.next 


        