from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        currLevel = 1
        nextLevel = 1
        q = deque()
        q.append(root)
        result = []

        while q:
            currLevel = nextLevel
            nextLevel=0
            result.append([])
            while currLevel > 0:
                node = q.pop()
                result[-1].append(node.val)
                currLevel-=1
                if node.left:
                    q.appendleft(node.left)
                    nextLevel+=1
                if node.right:
                    q.appendleft(node.right)
                    nextLevel+=1
        return result

