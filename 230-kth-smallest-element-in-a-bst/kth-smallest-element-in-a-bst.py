# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0 # instance variables so they retain their values across recursive calls.
        self.res = None
        self.inOrder(root,k)
        return self.res

    def inOrder(self, root,k):
        if not root:
            return
        
        self.inOrder(root.left,k)

        self.count += 1 # visit current node
        if self.count == k:
            self.res = root.val 
            return # stop further traversing

        self.inOrder(root.right,k)
    

