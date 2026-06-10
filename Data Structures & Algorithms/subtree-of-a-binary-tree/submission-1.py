# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checkSameTree(p, q) -> bool:
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return checkSameTree(p.left,q.left) and checkSameTree(p.right,q.right)
            return False
            
        def dfs(root, subRoot) -> bool:
            if not subRoot:
                return True
            if not root:
                return False
            if checkSameTree(root, subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)