# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#append,appendleft,pop,popleft
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        q = deque()
        result = []
        if root==None:
            return result
        q.append(root)
        while len(q)!=0:
            x = q[0]
            q.popleft()
            result.append(x.val)
            if x.left!=None:
                q.append(x.left)
            if x.right!=None:
                q.append(x.right)
        return result

