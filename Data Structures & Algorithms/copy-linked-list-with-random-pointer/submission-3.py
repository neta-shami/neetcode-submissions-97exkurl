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
            if p not in table:
                newNode = Node(p.val)
                pointer = newNode
                table[p] = pointer
            else:  
                newNode = table[p]
            
            if p.next == None:
                newNext = None
            elif p.next not in table:
                newNext = Node(p.next.val)
                pointer = newNext
                table[p.next] = pointer
            else:  
                newNext = table[p.next]
            newNode.next = newNext
            
            if p.random == None:
                newRandom = None
            elif p.random not in table:
                newRandom = Node(p.random.val)
                pointer = newRandom
                table[p.random] = pointer
            else:  
                newRandom = table[p.random]
            newNode.random = newRandom

            q.next = newNode
            q = q.next
            p = p.next

        return newHead.next 


        