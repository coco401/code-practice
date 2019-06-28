# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#we can use BFS or DFS

from collections import deque
    
class Solution:
    '''
    For BFS, we traverse the tree by level and check if the level is symmetric.
    '''
    def isSymmetric(self, root):
        if not root:
            return True
        
        result = self.BFS(root)
        return result
    
    def BFS(self, root):
        queue = deque([root])
        
        while(queue):
            level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: 
                    queue.append(node.left)
                else:
                    level.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    level.append(None)
                
            if level != level[::-1]:
                return False
            
        return True



root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.right.right=Node(3)

s=Solution()
print(s.isSymmetric(root))           