# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []

        if root.left:
            left_path = self.binaryTreePaths(root.left)
            for p in left_path:
                paths.append(str(root.val)+"->"+p)

        if root.right:
            right_path = self.binaryTreePaths(root.right)
            for p in right_path:
                paths.append(str(root.val)+"->"+p)        

        return paths