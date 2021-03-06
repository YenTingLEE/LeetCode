# Problem 106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) < 1:
            return None
        
        else:
            root = TreeNode(val=postorder[-1])
            IOIndex = inorder.index(root.val)
            POIndex = postorder.index(root.val)
            root.left = self.buildTree( inorder[0:IOIndex], postorder[0:IOIndex] )
            root.right = self.buildTree( inorder[IOIndex+1:], postorder[IOIndex:POIndex] )
        
            return root
