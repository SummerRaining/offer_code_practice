# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A==None or B==None:
            return False
        result = False
        if A.val == B.val:
            result = self.helper(A,B)
        result = result or self.isSubStructure(A.left,B)\
                or self.isSubStructure(A.right,B)
        return result

    def helper(self,A,B):
        result = False
        if B==None:
            return True
        if A==None:
            return False
        if A.val == B.val:
            result = self.helper(A.right,B.right)\
                     and self.helper(A.left,B.left)
        return result

