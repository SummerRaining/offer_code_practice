# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]: 
        q = deque()
        curN = 1
        nextN = 0
        layer,result = [],[]
        if root == None:
            return result
        q.append(root)
        while len(q)!=0:
            x = q[0]
            q.popleft()
            layer.append(x.val)
            curN -= 1
            if x.left != None:
                q.append(x.left)
                nextN += 1
            if x.right != None:
                q.append(x.right)
                nextN += 1

            if curN == 0:
                result.append(layer)
                curN = nextN
                nextN = 0
                layer = []
        return result
