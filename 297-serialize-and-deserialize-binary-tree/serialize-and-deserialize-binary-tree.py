# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")  # for None

        return ",".join(res)  # "1,2,3,null,null,4,5,null,null,null,null"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: # empty string
            return None 

        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = deque([root]) 
        i = 1
        while q:
            node = q.popleft()
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1

            if values[i] != "null":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1

        return root
        
    # class Codec: # recursive approach
    # def serialize(self, root):
    #     """Encodes a tree to a single string."""
    #     def dfs(node):
    #         if not node:
    #             return "null"
    #         return str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)

    #     return dfs(root)

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree."""
    #     def dfs(values):
    #         value = values.pop(0)
    #         if value == "null":
    #             return None
    #         node = TreeNode(int(value))
    #         node.left = dfs(values)
    #         node.right = dfs(values)
    #         return node

    #     values = data.split(",")
    #     return dfs(values)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
