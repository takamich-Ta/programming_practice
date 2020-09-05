# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def check(node,lower,upper):
            
            if node==None:
                return True
            
            val=node.val
            
            if val<=lower or val>=upper:
                return False
            
            if not check(node.right,val,upper):
                return False
            
            if not check(node.left,lower,val):
                return False
            
            
            return True
            
            
            
            
        return check(root,float("-inf"),float("inf"))
