# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def solve(root):
            nonlocal maxSum
            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)

            path1 = left + right + root.val
            path2 = max(left,right) + root.val
            path3 = root.val

            maxSum = max(maxSum,path1,path2,path3)

            return max(path2,path3)

        solve(root)
        return maxSum