# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = [0]  # Use a list to hold the index as a reference
        n = len(inorder)
        return self.solve(preorder,inorder,0,n-1,idx)

    def findPosition(self,inorder,element):
        for i in range(len(inorder)):
            if inorder[i] == element:
                return i
        return -1

    def solve(self,pre,inor,start,end,idx):
        if start > end:
            return None
        
        rootVal = pre[idx[0]]
        pos = self.findPosition(inor,rootVal)
        # Increment the index for the next recursive call
        idx[0] += 1
        root = TreeNode(rootVal)
        root.left = self.solve(pre,inor,start,pos-1,idx)
        root.right = self.solve(pre,inor,pos+1,end,idx)

        return root





