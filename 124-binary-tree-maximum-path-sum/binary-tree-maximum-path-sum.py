# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        self.solve(root)
        return self.maxSum

    def solve(self,root):
        if not root:
            return 0
        
        left = self.solve(root.left)
        right = self.solve(root.right)

        path1 = left + right + root.val
        path2 = max(left,right) + root.val
        path3 = root.val

        self.maxSum = max(self.maxSum,path1,path2,path3)

        return max(path2,path3)