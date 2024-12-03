class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        def helper(node, low, high):
            if not node:
                return True
            
            # Check if the current node's value is within the allowed range
            if not (low < node.val < high):
                return False
            
            return (helper(node.left, low, node.val) and 
                    helper(node.right, node.val, high))
        
        # Start the recursion with the entire range (-infinity to +infinity)
        return helper(root, float('-inf'), float('inf'))

# The left subtree has an upper bound of the current node's value.
# The right subtree has a lower bound of the current node's value.