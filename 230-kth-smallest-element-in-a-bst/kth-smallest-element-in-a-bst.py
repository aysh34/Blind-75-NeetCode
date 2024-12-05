# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 1st approach 
        res = self.inOrder(root)
        return res[k-1]
        # c = 1
        # for i in res:
        #     if c == k:
        #         return i
        #     else:
        #         c += 1
    
    def inOrder(self,root):
        if not root:
            return []
        return (
            self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
        ) # TC: O(n), SC: O(n) extra space

        # optimized approach
        
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

        self.inOrder(root.right,k) # SC: O(h) where h is the height of the tree. This is the space used by the recursion stack, which can be O(log n) for a balanced tree and O(n) for a skewed tree.
    

