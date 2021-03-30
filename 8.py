# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

#二叉树的下一个结点
class Solution:
    def GetNext(self, pNode):
        # write code here
        target = None
        if pNode.right != None:
            target = pNode.right
            while target.left!=None:
                target = target.left
        elif pNode.next != None:
            parent = pNode.next
            while parent!= None and parent.left != pNode:
                pNode = parent
                parent = parent.next
            if parent!=None:
                target = parent
        return target
