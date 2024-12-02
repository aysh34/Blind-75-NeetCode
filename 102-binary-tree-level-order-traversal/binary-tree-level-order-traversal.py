from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 
        
        res = []  
        q = deque([root])
        
        while q:
            levelSize = len(q)  
            level = []  # To store the values of the current level
            
            for _ in range(levelSize):
                pop = q.popleft()  
                level.append(pop.val)  # Add the value of the node to the current level
                
                # Add the children of the current node to the queue
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            
            res.append(level)  # Add the current level to the result
        
        return res
