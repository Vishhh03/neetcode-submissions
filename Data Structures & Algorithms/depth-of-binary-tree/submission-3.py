# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # #DFS Approach
        # def dfs(root) -> int:
        #     if not root:
        #         return 0
        #     return 1+(max(dfs(root.left),dfs(root.right)))
        # return dfs(root)

        #BFS Approach
        from collections import deque
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            depth += 1
        return depth
            


