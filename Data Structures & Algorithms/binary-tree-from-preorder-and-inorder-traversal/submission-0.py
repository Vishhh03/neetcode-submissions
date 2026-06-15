# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #
        # [1,2,3,4,5,6,7] -> Original Tree
        # [1,2,4,5,3,6,7] -> Preorder
        # [4,2,5,1,6,3,7] -> Inorder
        # Everything thats left of node in inorder in its left children and right of node is its right children
        # Recurse by passing the individual subtrees, since the pattern follows where everything left of the parent is its left children and same for right of parent
        # for each iteration we have to find the parents index in inorder to get its left and right children
        # how do we know who is the parent to find from inorder? 
        if not preorder:
            return None
        parent = preorder[0] 
        root = TreeNode(val=parent)
        parent_index = inorder.index(parent)
            
        root.left = self.buildTree(preorder[1:parent_index+1], inorder[:parent_index])
        root.right = self.buildTree(preorder[parent_index+1:], inorder[parent_index+1:])
        return root
