# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # def dfs(root):
        #     if not root:
        #         return
        #     root.left, root.right = root.right, root.left
        #     dfs(root.left)
        #     dfs(root.right)
        #     return root
        # return dfs(root)

        from collections import deque

        if not root:
            return root
        q = deque([root])
        returnroot = root
        while q:
            root = q.popleft()
            if root.left and root.right:
                root.left, root.right = root.right, root.left
                q.append(root.left)
                q.append(root.right)
        return returnroot



