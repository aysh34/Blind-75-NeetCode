# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inOrder(root)
        c = 1
        for i in res:
            if c == k:
                return i
            else:
                c += 1
    
    def inOrder(self,root):
        if not root:
            return []
        return (
            self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
        )