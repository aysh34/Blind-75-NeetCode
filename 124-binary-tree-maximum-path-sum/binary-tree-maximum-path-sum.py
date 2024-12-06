# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf') # initialized to negative infinity

        def solve(root):
            nonlocal maxSum # single shared maxSum variable across all recursive calls
            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)

            path1 = left + right + root.val # three paths represent all possible ways to use the current node in a path
            path2 = max(left,right) + root.val
            path3 = root.val

            maxSum = max(maxSum,path1,path2,path3)

            return max(path2,path3)

        solve(root)
        return maxSum
