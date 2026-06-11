# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        low = float('-inf')
        high = float('inf')
        def isValid(left, curr, right):
            if not curr:
                return True
            if left < curr.val < right:
                return isValid(curr.val, curr.right, right) and isValid(left, curr.left, curr.val)
            return False
        
        return isValid(low, root, high)        