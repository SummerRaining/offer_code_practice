# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        length = len(preorder)
        return self.helper(preorder,0,length-1,inorder,0,length-1)

    def helper(self,preorder,pleft,pright,inorder,ileft,iright):
        root = TreeNode(preorder[pleft])
        iileft = ileft
        while(iileft<=iright and inorder[iileft]!= root.val):
            iileft += 1
        l_length = iileft-ileft
        r_length = iright - iileft
        if l_length>0:
            root.left = self.helper(preorder,pleft+1,pleft+l_length,
                inorder,ileft,ileft+l_length-1)
        if r_length>0:
            root.right = self.helper(preorder,pleft+l_length+1,pright,
                inorder,ileft+l_length+1,iright)
        return root
