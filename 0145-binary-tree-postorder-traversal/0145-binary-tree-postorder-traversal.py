# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result = []
        def postorder(node):
            if not node:
                return
            postorder(node.left)       
            postorder(node.right)      
            result.append(node.val)    
        postorder(root)
        return result
        
        