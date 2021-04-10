# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        return self.helper(root,root)

    def helper(self,p1,p2):
        if p1==None and p2==None:
            return True
        if p1== None or p2== None:
            return False
        if p1.val==p2.val:
            return self.helper(p1.left,p2.right) \
                and self.helper(p1.right,p2.left)
        return False